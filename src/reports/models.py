from django.db import models

# Create your models here.


class SuspectedCase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_treated = models.BooleanField(default=False)

    def __str__(self):
        return "%s, " % self.date


class Declared(models.Model):
    date_declaration = models.DateTimeField(auto_now_add=True)
    id_treated = models.DateTimeField()

    def __str__(self):
        return "#%d, %s" % (self.pk, self.date_declaration)
