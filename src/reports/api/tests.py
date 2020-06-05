from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model

from attachments.models import Attachment
from geolocation.models import Town
from reports.models import SuspectedCase

from geolocation.models import State, Location, ReceptionCenter
from rest_framework.utils import json

from reports.api.serializers import SuspectedCaseSerializer

User = get_user_model()


class ReportTestCase(APITestCase):
    def setUp(self) -> None:
        user_obj = User(username="admin", email="abdennour@gmail.com")
        user_obj.set_password("admin")
        user_obj.save()
        self.token = user_obj.auth_token.key

        self.suspected_case = SuspectedCase.objects.create(
            attachment=Attachment.objects.create(
                nom="test attachment",
                extension="image",
                file="somefilehere",
            ),
            town=Town.objects.create(
                name="Batna",
                postal_code="05000",
                number_death=0,
                number_suspect=0,
                number_sick=0,
                number_confirmed_cases=0,
                number_carrier=0,
                number_recovered=0,
                state=State.objects.create(
                    name="Batna",
                    code=5,
                ),
                location=Location.objects.create(
                    longitude=1.4,
                    latitude=3.7,
                )
            ),
        )
        self.suspected_case.users.add(user_obj)
        self.suspected_case.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_suspected_case(self):
        count = SuspectedCase.objects.count()
        self.assertEqual(count, 1)

    def test_get_suspected_cases_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {}
        url = api_reverse("api-reports:suspected-cases-list")
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_suspected_case_object_bundle(self):
        """
        Test to verify suspected case object bundle
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        url = api_reverse("api-reports:suspected-cases-list")
        response = self.client.get(url)

        suspected_case_serialized_data = SuspectedCaseSerializer(instance=self.suspected_case).data
        suspected_case_serialized_data.pop('url', None)
        suspected_case_serialized_data.pop('attachment', None)
        suspected_case_serializer_data = [suspected_case_serialized_data]
        response_data = json.loads(response.content)
        response_data = list(filter(lambda a: a.pop('url', None), response_data))
        response_data = list(filter(lambda a: a.pop('attachment', None), response_data))
        self.assertEqual(suspected_case_serializer_data, response_data)

    def test_suspected_case_object_auth(self):
        """
        Test auth
        :return:
        """
        url = api_reverse("api-reports:suspected-cases-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)