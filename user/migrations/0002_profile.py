# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('name',
                 models.CharField(
                     max_length=255)),
                ('slug',
                 models.SlugField(
                     unique=True,
                     max_length=30)),
                ('about',
                 models.TextField()),
                ('joined',
                 models.DateTimeField(
                     verbose_name='Date Joined',
                     auto_now_add=True)),
                ('user',
                 models.OneToOneField(
                     to=settings.AUTH_USER_MODEL)
                 ),
            ],
        ),
    ]
