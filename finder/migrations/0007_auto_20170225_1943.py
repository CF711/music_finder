# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0006_auto_20170225_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.ManyToManyField(blank=True, to='finder.Album'),
        ),
    ]
