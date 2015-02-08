# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderer', '0005_auto_20150207_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='rating_avg',
        ),
        migrations.RemoveField(
            model_name='location',
            name='rating_count',
        ),
    ]
