from rest_framework import serializers
from ..models import SuspectedCase, Declared
from attachments.api.serializers import AttachmentSerializer
from attachments.models import Attachment


class SuspectedCaseSerializer(serializers.ModelSerializer):
    """

    SuspectedCase serializer.
    """
    attachment = AttachmentSerializer(required=True)

    class Meta:
        model = SuspectedCase
        fields = '__all__'

    def create(self, validated_data):
        attachment_data = validated_data.pop('attachment')
        attachment = Attachment.objects.create(**attachment_data)

        users_data = validated_data.pop('users')

        suspected_case = SuspectedCase.objects.create(attachment=attachment, **validated_data)
        suspected_case.users.add(*users_data)
        return suspected_case

    def update(self, instance, validated_data):
        suspected_case = SuspectedCase.objects.update(**validated_data)
        return suspected_case


class SuspectedCaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspectedCase
        fields = ['is_treated']


class DeclaredSerializer(serializers.ModelSerializer):
    """
    Declared serializer.
    """
    attachment = AttachmentSerializer(required=True)

    class Meta:
        model = Declared
        fields = '__all__'

    def create(self, validated_data):
        attachment_data = validated_data.pop('attachment')
        attachment = Attachment.objects.create(**attachment_data)

        users_data = validated_data.pop('users')

        declared = Declared.objects.create(attachment=attachment, **validated_data)
        declared.users.add(*users_data)
        return declared

    def update(self, instance, validated_data):
        suspected_case = SuspectedCase.objects.update(**validated_data)
        return suspected_case


class DeclaredUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declared
        fields = ['is_treated']
