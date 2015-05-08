# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.management import \
    create_permissions
from django.db import migrations, models


def generate_permissions(apps, schema_editor):
    Permission = apps.get_model(
        'auth', 'Permission')
    try:
        Permission.objects.get(
            codename='add_post',
            content_type__app_label='blog')
    except Permission.DoesNotExist:
        models_module = getattr(
            apps, 'models_module', None)
        if models_module is None:
            apps.models_module = True
            create_permissions(apps, verbosity=0)
            apps.models_module = None
        else:
            raise


def reverse_code(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('auth',
         '0006_require_contenttypes_0002'),
        ('blog',
         '0004_add_view_future_post_permission'),
    ]

    operations = [
        migrations.RunPython(
            generate_permissions,
            reverse_code,
        )
    ]
