# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def add_tag_data(apps, schema_editor):
    pass


def remove_tag_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_data,
            remove_tag_data)
    ]
