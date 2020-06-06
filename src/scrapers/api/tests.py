from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model

from rest_framework.utils import json

from scrapers.api.serializers import YoutubeVideoSerializer
from scrapers.models import YoutubeVideo

User = get_user_model()


class ScrapersTestCase(APITestCase):
    def setUp(self) -> None:
        user_obj = User(username="admin", email="abdennour@gmail.com")
        user_obj.set_password("admin")
        user_obj.save()
        self.token = user_obj.auth_token.key

        self.video = YoutubeVideo.objects.create(
            video_embed_url="https://www.youtube.com",
            video_id="test content",
            published_at="2020-01-01T00:00:00Z",
            title="video",
            channel_title="lol",
            description="lol",
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_video(self):
        video_count = YoutubeVideo.objects.count()
        self.assertEqual(video_count, 1)

    def test_get_videos_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {}
        url = api_reverse("api-scrapers:youtube-list")
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_video_object_bundle(self):
        """
        Test to verify article object bundle
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        url = api_reverse("api-scrapers:youtube-list")
        response = self.client.get(url)
        video_serialized_data = YoutubeVideoSerializer(instance=self.video).data
        video_serialized_data.pop('url', None)
        video_serializer_data = [video_serialized_data]
        response_data = json.loads(response.content)
        response_data = list(filter(lambda a: a.pop('url', None), response_data))
        self.assertEqual(video_serializer_data, response_data)

    def test_video_object_auth(self):
        """
        Test to verify auth in article object bundle
        :return:
        """
        url = api_reverse("api-scrapers:youtube-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
