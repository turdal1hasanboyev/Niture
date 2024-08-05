from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
