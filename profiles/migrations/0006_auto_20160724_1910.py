# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160722_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprofile',
            name='check_foursquare',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='check_foursquare',
            field=models.BooleanField(default=True),
        ),
    ]
