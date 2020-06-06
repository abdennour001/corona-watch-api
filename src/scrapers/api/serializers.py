from rest_framework import serializers
from ..models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    """

    """
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = YoutubeVideo
        fields = "__all__"

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)