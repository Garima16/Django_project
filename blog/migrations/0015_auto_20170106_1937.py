# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170106_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 14, 7, 36, 415613, tzinfo=utc)),
        ),
    ]
