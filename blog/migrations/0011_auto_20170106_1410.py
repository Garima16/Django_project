# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170106_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 8, 40, 40, 295486, tzinfo=utc)),
        ),
    ]
