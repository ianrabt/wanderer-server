# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderer', '0004_auto_20150207_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])),
                ('author', models.CharField(max_length=200)),
                ('location', models.ForeignKey(to='wanderer.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='rating_avg',
            field=models.DecimalField(decimal_places=10, blank=True, null=True, max_digits=11),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='rating_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perspective',
            name='author',
            field=models.CharField(max_length=200, default='anonymous'),
            preserve_default=False,
        ),
    ]
