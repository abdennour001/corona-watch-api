from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model

from feeds.models import Article
from attachments.models import Attachment
from rest_framework.utils import json

from feeds.api.serializers import ArticleSerializer

User = get_user_model()


class ArticleTestCase(APITestCase):
    def setUp(self) -> None:
        user_obj = User(username="admin", email="abdennour@gmail.com")
        user_obj.set_password("admin")
        user_obj.save()
        self.token = user_obj.auth_token.key

        self.article = Article.objects.create(
            title="test title",
            content="test content",
            publication_date="2020-01-01T00:00:00Z",
            attachment=Attachment.objects.create(
                nom="test attachment",
                extension="image",
                file="somefilehere",
            ),
            editor=user_obj
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_article(self):
        article_count = Article.objects.count()
        self.assertEqual(article_count, 1)

    def test_get_articles_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {}
        url = api_reverse("api-feeds:article-create")
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_object_bundle(self):
        """
        Test to verify article object bundle
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        url = api_reverse("api-feeds:article-create")
        response = self.client.get(url)

        article_serialized_data = ArticleSerializer(instance=self.article).data
        article_serialized_data.pop('url', None)
        article_serialized_data.pop('attachment', None)
        article_serializer_data = [article_serialized_data]
        response_data = json.loads(response.content)
        response_data = list(filter(lambda a: a.pop('url', None), response_data))
        response_data = list(filter(lambda a: a.pop('attachment', None), response_data))
        self.assertEqual(article_serializer_data, response_data)

    def test_article_object_auth(self):
        """
        Test to verify auth in article object bundle
        :return:
        """
        url = api_reverse("api-feeds:article-create")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
