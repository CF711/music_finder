# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_artist_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='finder.Song'),
        ),
    ]
