# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


def add_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    new_domain = 'site.django-unleashed.com'
    new_name = 'Startup Organizer'
    site_id = getattr(settings, 'SITE_ID', 1)
    if Site.objects.exists():
        current_site = Site.objects.get(
            pk=site_id)
        current_site.domain = new_domain
        current_site.name = new_name
        current_site.save()
    else:
        current_site = Site(
            pk=site_id,  # coerce primary key
            domain=new_domain,
            name=new_name)
        current_site.save()


def remove_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    current_site = Site.objects.get(
        pk=getattr(settings, 'SITE_ID', 1))
    current_site.domain = 'example.com'
    current_site.name = 'example.com'
    current_site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_site_data,
            remove_site_data,
        ),
    ]
