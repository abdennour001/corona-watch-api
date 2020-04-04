from django.db import models

# Create your models here.


class Region(models.Model):
    number_death = models.IntegerField()
    number_suspect = models.IntegerField()
    number_sick = models.IntegerField()
    radius = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    # centre

    def __str__(self):
        return "death: %s, suspect: %s, sick: %s" % (self.number_death, self.number_suspect, self.number_sick)


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return "%s, %s" % (self.longitude, self.latitude)


class ReceptionCenter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
