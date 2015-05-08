# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import \
    make_password
from django.db import migrations, models


def add_user_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model(
        'auth', 'Permission')
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('user', 'User')
    andrew_user = User.objects.create(
        email='django@jambonsw.com',
        password=make_password('hunter2'),
        is_active=True,
        is_staff=True,
        is_superuser=True)
    andrew_profile = Profile.objects.create(
        user=andrew_user,
        name='Andrew',
        slug='andrew',
        about='The author of this site!')
    # Django Girls is a real and very cool
    # organization but they are not affiliated
    # with this book and the email above is *not*
    # a real one.  Use of their name is for
    # illustrative purposes only.
    ada_user = User.objects.create(
        email='ada@djangogirls.org',
        password=make_password('algorhythm'),
        is_active=True,
        is_staff=True,
        is_superuser=False)
    ada_profile = Profile.objects.create(
        user=ada_user,
        name='Ada Lovelace',
        slug='the_countess',
        about=(
            'Django Girls is a non-profit '
            'organization that empowers and '
            'helps women to organize free, '
            'one-day programming workshops by '
            'providing tools, resources and '
            'support. It was born in Berlin and '
            'started by two Polish girls: Ola '
            'Sitarska and Ola Sendecka.'))
    contributors = Group.objects.create(
        name='contributors')
    ada_user.groups.add(contributors)
    permissions = [
        'add_post',
        'change_post',
    ]
    for perm in permissions:
        contributors.permissions.add(
            Permission.objects.get(
                codename=perm,
                content_type__app_label='blog'))


def remove_user_data(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('user', 'User')
    Profile.objects.get(slug='andrew').delete()
    Profile.objects.get(
        slug='the_countess').delete()
    User.objects.get(
        email='django@jambonsw.com').delete()
    User.objects.get(
        email='ada@djangogirls.org').delete()
    Group.objects.get(
        name='contributors').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_permissions'),
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.RunPython(
            add_user_data,
            remove_user_data)
    ]
