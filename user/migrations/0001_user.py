# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth',
            '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id',
                 models.AutoField(
                     serialize=False,
                     verbose_name='ID',
                     auto_created=True,
                     primary_key=True)),
                ('password',
                 models.CharField(
                     max_length=128,
                     verbose_name='password')),
                ('last_login',
                 models.DateTimeField(
                     blank=True,
                     verbose_name='last login',
                     null=True)),
                ('is_superuser',
                 models.BooleanField(
                     help_text=(
                         'Designates that this '
                         'user has all '
                         'permissions without '
                         'explicitly assigning '
                         'them.'),
                     verbose_name=(
                         'superuser status'),
                     default=False)),
                ('email',
                 models.EmailField(
                     unique=True,
                     max_length=254,
                     verbose_name=(
                         'email address'))),
                ('is_staff',
                 models.BooleanField(
                     help_text=(
                         'Designates whether the '
                         'user can log into this '
                         'admin site.'),
                     verbose_name='staff status',
                     default=False)),
                ('is_active',
                 models.BooleanField(
                     help_text=(
                         'Designates whether '
                         'this user should be '
                         'treated as active. '
                         'Unselect this instead '
                         'of deleting accounts.'),
                     verbose_name='active',
                     default=True)),
                ('groups',
                 models.ManyToManyField(
                     help_text=(
                         'The groups this user '
                         'belongs to. A user will '
                         'get all permissions '
                         'granted to each of '
                         'their groups.'),
                     blank=True,
                     to='auth.Group',
                     verbose_name='groups',
                     related_name='user_set',
                     related_query_name='user')),
                ('user_permissions',
                 models.ManyToManyField(
                     help_text=(
                         'Specific permissions '
                         'for this user.'),
                     blank=True,
                     to='auth.Permission',
                     verbose_name=(
                         'user permissions'),
                     related_name='user_set',
                     related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects',
                 user.models.UserManager()),
            ],
        ),
    ]
