from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


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
    image_url = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return super().__str__()


class MedicalProfile(models.Model):
    weight = models.FloatField(null=True)
    temperature = models.FloatField(null=True)
    is_suspect = models.BooleanField(null=True)
    date = models.DateTimeField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (Kg), %s (C), %s" % (self.weight, self.temperature, self.is_suspect)


# whenever user is created, give it a medical profile and a token
@receiver(post_save, sender=User)
def create_user_medical_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'final user':
        MedicalProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_medical_profile(sender, instance, **kwargs):
    if instance.role == 'final user':
        instance.medicalprofile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
