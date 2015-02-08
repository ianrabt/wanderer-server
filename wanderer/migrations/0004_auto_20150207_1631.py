# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderer', '0003_auto_20150207_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(max_digits=9, decimal_places=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(max_digits=9, decimal_places=6),
            preserve_default=True,
        ),
    ]
