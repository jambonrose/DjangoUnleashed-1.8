# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_author'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='post',
            index_together=set(
                [('slug', 'pub_date')]),
        ),
    ]
