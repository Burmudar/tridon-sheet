# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0009_auto_20160826_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbookentry',
            name='consignee',
            field=models.CharField(max_length=255, verbose_name='Consignee Name'),
        ),
    ]
