from rest_framework import serializers
from feeds.models import Article, Video, Comment


class ArticleSerializer(serializers.ModelSerializer):
    """
    Main objective of this class is to:
        1. Convert data to valid JSON format.
        2. Validate data passed and sent.
    """
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'is_deleted',
            'publication_date',
            'attachment',
            'editor'
        ]

    @staticmethod
    def validate_title(value):
        # some logic to validate the title value.
        return value


class VideoSerializer(serializers.ModelSerializer):
    """
    Video Serializer.
    """
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'is_deleted',
            'publication_date',
            'attachment',
            'user',
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer.
    """

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
