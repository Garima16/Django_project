# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 18:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountHolder',
        ),
    ]