from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL)
    slug = models.SlugField(
        max_length=30,
        unique=True)
    about = models.TextField()

    def __str__(self):
        return self.user.get_username()
