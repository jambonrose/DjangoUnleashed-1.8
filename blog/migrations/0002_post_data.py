# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import migrations, models

POSTS = [
    {
        "title": "Django 1.0 Release",
        "slug": "django-10-released",
        "pub_date": date(2008, 9, 3),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text": "THE Web Framework.",
    },
    {
        "title": "Simple Robots for Sale",
        "slug": "simple-robots-for-sale",
        "pub_date": date(2011, 2, 21),
        "startups": ["simple-robots"],
        "tags": ["augmented-reality", "python"],
        "text":
            "If only they would make "
            "spider bots.",
    },
    {
        "title": "Django Training",
        "slug": "django-training",
        "pub_date": date(2013, 1, 18),
        "startups": ["jambon-software"],
        "tags": ["django"],
        "text":
            "Want to learn Django in a class "
            "setting? JamBon Software offers "
            "hands-on courses in the web "
            "framework. Just looking for help? "
            "They'll consult on your web and "
            "mobile products and can also be "
            "hired for end-to-end development.",
    },
    {
        "title": "Django 1.8 Release",
        "slug": "django-18-released",
        "pub_date": date(2015, 4, 1),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text": "Django 1.8 is Django's newest "
            "version, and the next version "
            "slated for Long-Term Support "
            "(LTS). LTS means that Django 1.8 "
            "will be supported for longer than "
            "regular versions: Django core "
            "developers will specify a single "
            "release as LTS, and then continue "
            "to update that version regardless "
            "of the usual release cycle. This "
            "will last until they pick a new "
            "LTS version, which typically "
            "happens every 3 to 4 years. The "
            "last LTS version was 1.4, "
            "released in March 2012, which "
            "will stop being supported in "
            "October 2015.\n\n"
            "For more information: \n"
            "http://andrewsforge.com/article/"
            "upgrading-django-to-17/part-1-"
            "introduction-and-django-releases/",
    },
    {
        "title": "More Django Info",
        "slug": "more-django-info",
        "pub_date": date(2015, 4, 8),
        "startups": ["jambon-software"],
        "tags": ["django", "web"],
        "text":
            "Remember that the official websites "
            "for Django and this book contain a "
            "number of extra resources.\n\n"
            "https://djangoproject.com\n"
            "https://django-unleashed.com\n\n"
            "Want more Django info? "
            "There's always my personal blog!\n\n"
            "https://AndrewsForge.com",
    },
    {
        "title": "New Django Version",
        "slug": "new-django-version",
        "pub_date": date(2020, 5, 15),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text":
            "Better integration with "
            "HTML Boilerstrap 9.",
    },
]


def add_post_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Startup = apps.get_model(
        'organizer', 'Startup')
    Tag = apps.get_model('organizer', 'Tag')
    for post_dict in POSTS:
        post = Post.objects.create(
            title=post_dict['title'],
            slug=post_dict['slug'],
            text=post_dict['text'])
        post.pub_date = post_dict['pub_date']
        post.save()
        for tag_slug in post_dict['tags']:
            post.tags.add(
                Tag.objects.get(
                    slug=tag_slug))
        for startup_slug in post_dict['startups']:
            post.startups.add(
                Startup.objects.get(
                    slug=startup_slug))


def remove_post_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post_dict in POSTS:
        post = Post.objects.get(
            slug=post_dict['slug'])
        post.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('organizer', '0003_startup_data'),
    ]

    operations = [
        migrations.RunPython(
            add_post_data,
            remove_post_data)
    ]
