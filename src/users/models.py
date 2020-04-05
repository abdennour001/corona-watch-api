from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    """auth/login-related fields"""

    ROLE = (
        ('final user', 'The final user (Android user).'),
        ('health agent', 'The health agent.'),
        ('moderator', 'The Moderator.'),
        ('editor', 'The editor of articles'),
    )
    role = models.CharField(
        max_length=32,
        choices=ROLE,
        default='final user'
    )
    image_url = models.URLField(default=None)

    def __str__(self):
        super(User, self).__str__()


class MedicalProfile(models.Model):
    weight = models.FloatField()
    temperature = models.FloatField()
    is_suspect = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (Kg), %s (C), %s" % (self.weight, self.temperature, self.is_suspect)
