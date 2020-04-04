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

    def __str__(self):
        super(User, self).__str__()
