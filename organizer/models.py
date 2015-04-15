from django.db import models


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class Tag(models.Model):
    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.')


class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()
    tags = models.ManyToManyField(Tag)


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()
    startup = models.ForeignKey(Startup)
