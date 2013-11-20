from django.db import models

from organizer.models import Startup, Tag


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
