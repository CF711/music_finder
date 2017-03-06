# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-27 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0014_auto_20170226_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifferentArtistVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SameArtistVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='other_artist_linked_songs',
        ),
        migrations.RemoveField(
            model_name='song',
            name='same_artist_linked_songs',
        ),
    ]
