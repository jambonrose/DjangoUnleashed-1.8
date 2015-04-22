# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import reduce
from operator import or_

from django.db import migrations, models
from django.db.models import Q

TAGS = (
    # ( tag name, tag slug ),
    ("augmented reality", "augmented-reality"),
    ("big data", "big-data"),
    ("django", "django"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("mobile", "mobile"),
    ("node.js", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
    ("video games", "video-games"),
    ("web", "web"),
    ("zend", "zend"),
)


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')
    tag_list = []
    for tag_name, tag_slug in TAGS:
        tag_list.append(
            Tag(name=tag_name, slug=tag_slug))
    Tag.objects.bulk_create(tag_list)


def remove_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')
    query_list = []
    for _, tag_slug in TAGS:
        query_list.append(
            Q(slug=tag_slug))
    query = reduce(or_, query_list)
    Tag.objects.filter(query).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_data,
            remove_tag_data)
    ]
