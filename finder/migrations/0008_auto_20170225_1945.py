# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0007_auto_20170225_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_of_linked_songs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='songs',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='album_artist', chained_model_field='artist', to='finder.Song'),
        ),
    ]
