# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(
            settings.AUTH_USER_MODEL),
        ('blog',
         '0005_post_permissions'),
        ('user',
         '0003_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                default=1,
                related_name='blog_posts',
                to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
