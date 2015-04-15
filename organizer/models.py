from django.db import models


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()


class Startup(models.Model):
    pass


class NewsLink(models.Model):
    pass
