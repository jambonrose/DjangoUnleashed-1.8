# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id',
                 models.AutoField(
                     serialize=False,
                     verbose_name='ID',
                     auto_created=True,
                     primary_key=True)),
                ('title',
                 models.CharField(max_length=63)),
                ('slug',
                 models.SlugField(
                     max_length=63,
                     unique_for_month='pub_date',
                     help_text='A label for URL config')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(
                    verbose_name='date published',
                    auto_now_add=True)),
                ('startups', models.ManyToManyField(
                    to='organizer.Startup',
                    related_name='blog_posts')),
                ('tags', models.ManyToManyField(
                    to='organizer.Tag',
                    related_name='blog_posts')),
            ],
            options={
                'ordering': [
                    '-pub_date', 'title'],
                'verbose_name': 'blog post',
                'get_latest_by': 'pub_date',
            },
        ),
    ]
