from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.utils import json
import requests


class YoutubeSearch(APIView):
    """
    View to search in Youtube videos using keywords like (#covide-19, #covid, ...)
    """
    def get(self, request, format=None):
        """
        Return list of youtube search videos.
        :return:
        """
        response = []
        api_key = settings.YOUTUBE_API_KEY
        query = request.GET.get('q')
        max_results = request.GET.get('maxResults')
        youtube_api_response = requests.get(
            f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&type=video&maxResults={max_results}"
        )
        for item in youtube_api_response.json()['items']:
            response.append({
                "video_embed_url": f"http://www.youtube.com/embed/{item.get('id').get('videoId')}",
                "video_id": item.get('id').get('videoId'),
                "video_metadata": {
                    'published_at': item.get("snippet").get("publishedAt"),
                    'title': item.get("snippet").get("title"),
                    'description': item.get("snippet").get("description"),
                    'channel_title': item.get("snippet").get("channelTitle"),
                }
            })
        return Response(json.loads(json.dumps(response)))
