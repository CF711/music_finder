# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-26 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default='TEST', max_length=255),
            preserve_default=False,
        ),
    ]
