from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializerCreate, UserSerializerOut, MedicalProfileSerializer
from ..models import User, MedicalProfile
from rest_framework import generics
from django.http import Http404
from django.db.models import Q


class UserList(generics.ListAPIView):
    """
    Generic class based view to list users.
    You can use GET VARIABLES to specify the role of the users.
    ===> role=<user_role>
    """
    serializer_class = UserSerializerOut

    def get_queryset(self):
        queryset = User.objects.all()
        role = self.request.GET.get('role')
        if role is not None:
            queryset = queryset.filter(
                Q(role__exact=role)
            ).distinct()
        return queryset


class UserDetail(generics.RetrieveAPIView):
    """
    Generic class based view detail of the user.
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializerOut


class UserMedicalProfileDetail(generics.RetrieveAPIView):
    """
    get:
    Return user's medical profile.
    """
    lookup_field = 'username'
    serializer_class = MedicalProfileSerializer
    # queryset = MedicalProfile.objects.all()

    def get_object(self):
        username = self.kwargs.get("username")
        try:
            user = User.objects.get(username=username)
            return user.medicalprofile
        except User.DoesNotExist:
            raise Http404
        except MedicalProfile.DoesNotExist:
            raise Http404


class UserCreate(generics.CreateAPIView):
    """
    post:
    Create a new user
    """
    serializer_class = UserSerializerCreate

    def post(self, request, *args, **kwargs):
        response = self.create(request, args, kwargs)
        user = response.data
        return Response({
            "username": user.get("username"),
            "email": user.get("email"),
            "role": user.get("role"),
        })


class UserAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'role': user.role,
        }
        if user.image_url is not None:
            response['image_url'] = user.image_url,
        if user.role == "final user":
            response['medical_profile'] = MedicalProfileSerializer(user.medicalprofile).data
        return Response(response)
