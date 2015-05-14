from datetime import date

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin)
from django.core.urlresolvers import reverse
from django.db import models


class ProfileManager(models.Manager):

    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


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

    objects = ProfileManager()

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse(
            'dj-auth:public_profile',
            kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('dj-auth:profile_update')

    def natural_key(self):
        return (self.slug,)
    natural_key.dependencies = ['user.user']


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self, email, password, **kwargs):
        email = self.normalize_email(email)
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop(
            'is_superuser', False)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self, email, password=None,
            **extra_fields):
        return self._create_user(
            email, password, **extra_fields)

    def create_superuser(
            self, email, password,
            **extra_fields):
        return self._create_user(
            email, password,
            is_staff=True, is_superuser=True,
            **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


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

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return self.profile.get_absolute_url()

    def get_full_name(self):
        return self.profile.name

    def get_short_name(self):
        return self.profile.name

    def published_posts(self):
        return self.blog_posts.filter(
            pub_date__lt=date.today())

    def natural_key(self):
        return (self.email,)
