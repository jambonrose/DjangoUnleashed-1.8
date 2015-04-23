# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import migrations, models

NEWSLINKS = [
    {
        "title": "Redundant Homepage Link",
        "link": "http://jambonsw.com",
        "pub_date": date(2013, 1, 18),
        "startup": 'jambon-software',
    },
    {
        "title": "Monkey (Wikipedia)",
        "link": "https://en.wikipedia.org/wiki/Monkey",
        "pub_date": date(2012, 7, 22),
        "startup": "monkey-software",
    },
    {
        "title": "William Shakespeare (Wikipedia)",
        "link": "https://en.wikipedia.org/wiki/William_Shakespeare",
        "pub_date": date(2014, 4, 26),
        "startup": "monkey-software",
    },
]


def add_newslink_data(apps, schema_editor):
    NewsLink = apps.get_model(
        'organizer', 'NewsLink')
    Startup = apps.get_model(
        'organizer', 'Startup')
    for newslink_dict in NEWSLINKS:
        newslink = NewsLink.objects.create(
            title=newslink_dict['title'],
            link=newslink_dict['link'],
            pub_date=newslink_dict['pub_date'],
            startup=Startup.objects.get(
                slug=newslink_dict['startup']))


def remove_newslink_data(apps, schema_editor):
    NewsLink = apps.get_model(
        'organizer', 'NewsLink')
    Startup = apps.get_model(
        'organizer', 'Startup')
    for newslink_dict in NEWSLINKS:
        newslink = NewsLink.objects.get(
            title=newslink_dict['title'],
            link=newslink_dict['link'],
            pub_date=newslink_dict['pub_date'],
            startup=Startup.objects.get(
                slug=newslink_dict['startup']),
        )
        newslink.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_startup_data'),
    ]

    operations = [
        migrations.RunPython(
            add_newslink_data,
            remove_newslink_data)
    ]
