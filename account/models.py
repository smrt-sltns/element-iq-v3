from django.db import models

from django.contrib.auth.models import AbstractUser


# custom user model in case we need to change the user
class User(AbstractUser):
    pass