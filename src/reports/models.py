from django.db import models

# Create your models here.


class SuspectedCase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_treated = models.BooleanField(default=False)

    def __str__(self):
        return "%s, " % self.date


class Declared(models.Model):
    weight = models.FloatField()
    temperature = models.FloatField()
    is_suspect = models.BooleanField()

    def __str__(self):
        return "%s (Kg), %s (C), %s" % (self.weight, self.temperature, self.is_suspect)
