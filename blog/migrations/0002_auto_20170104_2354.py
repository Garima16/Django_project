# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-04 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 18, 24, 29, 325260, tzinfo=utc)),
        ),
    ]
