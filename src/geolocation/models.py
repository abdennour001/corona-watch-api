from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    reception_center = models.ForeignKey('ReceptionCenter', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s, %s" % (self.longitude, self.latitude)


class State(models.Model):
    name = models.CharField(max_length=128)
    code = models.IntegerField()

    def __str__(self):
        return f"[{ self.code }] { self.name }"


class Town(models.Model):
    name = models.CharField(max_length=512)
    postal_code = models.CharField(max_length=10)
    number_death = models.IntegerField()
    number_suspect = models.IntegerField()
    number_sick = models.IntegerField()
    number_confirmed_cases = models.IntegerField()
    number_carrier = models.IntegerField()
    number_recovered = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    is_risked = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)

    state = models.ForeignKey(State, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "Town: [%s] %s, death: %s, suspect: %s, sick: %s" % (self.postal_code, self.name, self.number_death, self.number_suspect, self.number_sick)


class Region(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    admins = models.ManyToManyField(get_user_model())
    states = models.ManyToManyField(State)

    def __str__(self):
        return f"{ self.name } - { self.description }"


class ReceptionCenter(models.Model):
    name = models.CharField(max_length=100)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
