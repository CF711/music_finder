# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0013_auto_20170226_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_art',
            field=models.ImageField(blank=True, upload_to='albums'),
        ),
    ]
