from django.db import models

# Create your models here.


class Attachment(models.Model):
    EXTENSIONS = (
        ('image', 'Image Type'),
        ('video', 'Video Type'),
    )
    nom = models.CharField(max_length=256)
    extension = models.CharField(
        max_length=32,
        choices=EXTENSIONS,
        default='image'
    )
    file = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.nom, self.extension)
