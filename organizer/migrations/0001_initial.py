# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id',
                 models.AutoField(
                     primary_key=True,
                     verbose_name='ID',
                     auto_created=True,
                     serialize=False)),
                ('title',
                 models.CharField(max_length=63)),
                ('pub_date', models.DateField(
                    verbose_name='Date Published')),
                ('link',
                 models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'news article',
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id',
                 models.AutoField(
                     primary_key=True,
                     verbose_name='ID',
                     auto_created=True,
                     serialize=False)),
                ('name', models.CharField(
                    db_index=True, max_length=31)),
                ('slug',
                 models.SlugField(
                     max_length=31,
                     unique=True,
                     help_text='A label for URL config.')),
                ('description',
                 models.TextField()),
                ('founded_date', models.DateField(
                    verbose_name='Date Founded')),
                ('contact',
                 models.EmailField(max_length=254)),
                ('website',
                 models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id',
                 models.AutoField(
                     primary_key=True,
                     verbose_name='ID',
                     auto_created=True,
                     serialize=False)),
                ('name', models.CharField(
                    unique=True, max_length=31)),
                ('slug',
                 models.SlugField(
                     max_length=31,
                     unique=True,
                     help_text='A label for URL config.')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(
                to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(
                to='organizer.Startup'),
        ),
    ]
