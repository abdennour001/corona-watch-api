from django.db import models
from django.contrib.auth import get_user_model
from attachments.models import Attachment
from geolocation.models import Town

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


class Declared(models.Model):
    date_declaration = models.DateTimeField(auto_now_add=True)
    id_treated = models.DateTimeField()
    attachment = models.OneToOneField(
        Attachment,
        on_delete=models.CASCADE,
        null=True,
    )
    users = models.ManyToManyField(get_user_model())

    def __str__(self):
        return "#%d, %s" % (self.pk, self.date_declaration)
