# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-19 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userDetails', '0002_auto_20161219_1947'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddres',
            new_name='UserAddress',
        ),
    ]
