# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 06:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0010_remove_album_num_of_linked_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finder.Album'),
            preserve_default=False,
        ),
    ]
