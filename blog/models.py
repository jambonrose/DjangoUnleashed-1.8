from django.db import models


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
