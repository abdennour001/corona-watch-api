from rest_framework import serializers
from ..models import SuspectedCase, Declared
from attachments.api.serializers import AttachmentSerializer, AttachmentSerializerUploaded
from attachments.models import Attachment


class SuspectedCaseSerializer(serializers.ModelSerializer):
    """

    SuspectedCase serializer.
    """
    url = serializers.SerializerMethodField(read_only=True)
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

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class SuspectedCaseSerializerUploaded(serializers.ModelSerializer):
    """
    SuspectedCase serializer from uploaded video.
    """
    url = serializers.SerializerMethodField(read_only=True)
    attachment = AttachmentSerializerUploaded(required=True)

    class Meta:
        model = SuspectedCase
        fields = "__all__"

    def create(self, validated_data):
        attachment_data = validated_data.pop('attachment')
        attachment = Attachment()
        attachment.nom = attachment_data["nom"]
        attachment.extension = attachment_data["extension"]
        attachment.file = attachment_data["file"]
        attachment.save()
        #attachment = Attachment.objects.create(**attachment_data)

        users_data = validated_data.pop('users')

        suspected_case = SuspectedCase.objects.create(attachment=attachment, **validated_data)
        suspected_case.users.add(*users_data)
        return suspected_case

    def update(self, instance, validated_data):
        suspected_case = SuspectedCase.objects.update(**validated_data)
        return suspected_case

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


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
