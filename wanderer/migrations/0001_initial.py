# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200, default='unknown', blank=True)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perspective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='photo')),
                ('date', models.DateTimeField()),
                ('author', models.CharField(null=True, max_length=200, blank=True)),
                ('location', models.ForeignKey(to='wanderer.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
