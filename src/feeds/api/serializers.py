from rest_framework import serializers
from ..models import Article, Video, Comment, Publication
from attachments.api.serializers import AttachmentSerializer
from attachments.models import Attachment


class ArticleSerializer(serializers.ModelSerializer):
    """
    Main objective of this class is to:
        1. Convert data to valid JSON format.
        2. Validate data passed and sent.
    """

    url = serializers.SerializerMethodField(read_only=True)
    attachment = AttachmentSerializer(required=True)

    class Meta:
        model = Article
        fields = [
            'url',
            'id',
            'title',
            'content',
            'is_deleted',
            'is_validated',
            'publication_date',
            'attachment',
            'editor'
        ]

    @staticmethod
    def validate_title(value):
        # some logic to validate the title value.
        return value

    def create(self, validated_data):
        attachment_data = validated_data.pop('attachment')
        attachment = Attachment.objects.create(**attachment_data)

        article = Article.objects.create(attachment=attachment, **validated_data)
        return article

    def update(self, instance, validated_data):
        article = Article.objects.update(**validated_data)
        return article

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'is_deleted',
            'is_validated',
        ]


class VideoSerializer(serializers.ModelSerializer):
    """
    Video Serializer.
    """

    attachment = AttachmentSerializer(required=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'is_deleted',
            'is_validated',
            'publication_date',
            'attachment',
            'user',
        ]


class VideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'is_deleted',
            'is_validated',
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer.
    """

    publication = serializers.ReadOnlyField(source='publication.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'comment_date',
            'is_deleted',
            'user',
            'publication',
        ]


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
