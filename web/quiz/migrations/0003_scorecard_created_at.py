# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 04:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_scorecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecard',
            name='created_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 4, 9, 4, 19, 32, 717773, tzinfo=utc)),
            preserve_default=False,
        ),
    ]