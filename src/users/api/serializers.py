from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import User, MedicalProfile


class UserSerializerOut(serializers.ModelSerializer):
    """
    Serializer for when data needs for GET purposes.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'image_url')


class UserSerializerCreate(serializers.ModelSerializer):
    """
    Serializer for creating an account.
    """

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role', 'image_url')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MedicalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProfile
        fields = '__all__'
