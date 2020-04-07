from rest_framework import serializers
from feeds.models import Article


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
