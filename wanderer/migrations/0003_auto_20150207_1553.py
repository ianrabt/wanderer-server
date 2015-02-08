# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderer', '0002_perspective_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perspective',
            name='photo',
            field=models.ImageField(upload_to='photos'),
            preserve_default=True,
        ),
    ]
