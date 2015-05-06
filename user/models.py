from django.conf import settings
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        return reverse(
            'dj-auth:public_profile',
            kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('dj-auth:profile_update')
