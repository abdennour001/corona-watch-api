from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import SuspectedCase, Declared
from .serializers import SuspectedCaseSerializer, SuspectedCaseUpdateSerializer, DeclaredSerializer, \
    DeclaredUpdateSerializer, SuspectedCaseSerializerUploaded


class SuspectedCaseCreateListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all reports that exists.

    post:
    Report a new suspected case in the system.
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}


class SuspectedCaseCreateFromUploaded(generics.CreateAPIView):
    """
    post:
    Report a new suspected case in the system, the attachment file .
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializerUploaded
    queryset = SuspectedCase.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}


class SuspectedCaseRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    get:
    Get the suspected case with ( pk="id" ).

    delete:
    Delete the suspected case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()

    def get_serializer_context(self):
        return {"request": self.request}


class SuspectedCaseUpdateView(generics.UpdateAPIView):
    """
    put:
    Update the suspected case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseUpdateSerializer
    queryset = SuspectedCase.objects.all()


class DeclaredCreateListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all Declared that exists.

    post:
    Report a new Declared case in the system.
    """
    lookup_field = 'id'
    serializer_class = DeclaredSerializer
    queryset = Declared.objects.all()


class DeclaredRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    get:
    Get the Declared case with ( pk="id" ).

    delete:
    Delete the Declared case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = DeclaredSerializer
    queryset = Declared.objects.all()


class DeclaredUpdateView(generics.UpdateAPIView):
    """
    put:
    Update the Declared case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = DeclaredUpdateSerializer
    queryset = Declared.objects.all()

