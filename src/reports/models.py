from django.db import models
from django.contrib.auth import get_user_model
from attachments.models import Attachment
from geolocation.models import Town
from rest_framework.reverse import reverse as api_reverse

# Create your models here.


class SuspectedCase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_treated = models.BooleanField(default=False)
    attachment = models.OneToOneField(
        Attachment,
        on_delete=models.CASCADE,
        null=True,
    )
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    users = models.ManyToManyField(get_user_model())

    def __str__(self):
        return "%s, " % self.date

    def get_api_url(self, request=None):
        return api_reverse("api-reports:suspected-cases-RUD", kwargs={'id': self.pk}, request=request)


class Declared(models.Model):
    date_declaration = models.DateTimeField(auto_now_add=True)
    is_treated = models.BooleanField(default=False)
    attachment = models.OneToOneField(
        Attachment,
        on_delete=models.CASCADE,
        null=True,
    )
    users = models.ManyToManyField(get_user_model())

    def __str__(self):
        return "#%d, %s" % (self.pk, self.date_declaration)
