# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-05 14:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170104_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 5, 14, 13, 38, 800837, tzinfo=utc)),
        ),
    ]
