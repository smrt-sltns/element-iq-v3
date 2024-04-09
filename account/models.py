from django.db import models

from django.contrib.auth.models import AbstractUser


# custom user model in case we need to change the user
class User(AbstractUser):
    token = models.IntegerField(default=0)
    stripe_session = models.CharField(max_length=255, default="", null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.email}"