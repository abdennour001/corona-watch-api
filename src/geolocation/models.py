from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    reception_center = models.ForeignKey('ReceptionCenter', on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.longitude, self.latitude)


class Region(models.Model):
    number_death = models.IntegerField()
    number_suspect = models.IntegerField()
    number_sick = models.IntegerField()
    number_confirmed_cases = models.IntegerField()
    number_carrier = models.IntegerField()
    number_recovered = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=512)
    is_risked = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    admins = models.ManyToManyField(get_user_model())

    def __str__(self):
        return "death: %s, suspect: %s, sick: %s" % (self.number_death, self.number_suspect, self.number_sick)


class ReceptionCenter(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
