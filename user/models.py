from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin)
from django.core.urlresolvers import reverse
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL)
    name = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=30,
        unique=True)
    about = models.TextField()
    joined = models.DateTimeField(
        "Date Joined",
        auto_now_add=True)

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse(
            'dj-auth:public_profile',
            kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('dj-auth:profile_update')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            'Designates whether the user can '
            'log into this admin site.'))
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should '
            'be treated as active. Unselect this '
            'instead of deleting accounts.'))

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return self.profile.get_absolute_url()

    def get_full_name(self):
        return self.profile.name

    def get_short_name(self):
        return self.profile.name
