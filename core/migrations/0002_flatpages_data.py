# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

FLATPAGES = [
    {
        "title": "About",
        "url": "/about/",
        "content":
            '<p>This website is built in <a '
            'href="'
            'https://www.djangoproject.com">'
            'Django</a>, '
            'and is the basis of the code in the'
            ' book <a '
            'href="http://www.amazon.com/'
            'Django-Unleashed-Andrew-Pinkham/'
            'dp/0321985079">'
            'Django Unleashed</a>, written by <a '
            'href="https://AndrewsForge.com/">'
            'Andrew Pinkham</a>.</p>\n'
            '<p>The site design is based on the '
            'CSS boilerplate <a '
            'href="http://getskeleton.com">'
            'Skeleton</a>, '
            'and makes use of HTML from <a '
            'href="https://html5boilerplate.com">'
            'HTML5 Boilerplate</a> as well as <a '
            'href="http://csswizardry.com/2011/'
            '01/the-real-html5-boilerplate/">'
            'Harry Robert\'s HTML5 boilerplate'
            '</a>.</p>'
    },
]


def add_flatpages_data(apps, schema_editor):
    FlatPage = apps.get_model(
        'flatpages', 'FlatPage')
    Site = apps.get_model('sites', 'Site')
    site_id = getattr(settings, 'SITE_ID', 1)
    current_site = Site.objects.get(pk=site_id)
    for page_dict in FLATPAGES:
        new_page = FlatPage.objects.create(
            title=page_dict['title'],
            url=page_dict['url'],
            content=page_dict['content'])
        new_page.sites.add(current_site)


def remove_flatpages_data(apps, schema_editor):
    FlatPage = apps.get_model(
        'flatpages', 'FlatPage')
    for page_dict in FLATPAGES:
        page = FlatPage.objects.get(
            url=page_dict['url'])
        page.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_sites_data'),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_flatpages_data,
            remove_flatpages_data,
        ),
    ]
