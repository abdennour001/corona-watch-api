from rest_framework import serializers
from ..models import SuspectedCase
from attachments.api.serializers import AttachmentSerializer


class SuspectedCaseSerializer(serializers.ModelSerializer):
    """
    SuspectedCase serializer.
    """
    attachment = AttachmentSerializer(required=True)

    class Meta:
        model = SuspectedCase
        fields = '__all__'
