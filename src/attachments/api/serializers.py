from rest_framework import serializers
from ..models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    """
    Attachment serializer.
    """
    class Meta:
        model = Attachment
        fields = '__all__'


class AttachmentSerializerUploaded(serializers.ModelSerializer):
    """
    Attachment serializer uploaded.
    """

    file = serializers.CharField(max_length=2000)

    class Meta:
        model = Attachment
        fields = [
            'id',
            'nom',
            'extension',
            'date',
            'file'
        ]

    @staticmethod
    def validate_file(file):
        """
        Check that file is a string url.
        """
        if not isinstance(file, str):
            raise serializers.ValidationError("file must be a string.")
        return file
