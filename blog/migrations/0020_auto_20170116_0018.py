# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 18:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170115_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 15, 18, 48, 9, 754411, tzinfo=utc)),
        ),
    ]
