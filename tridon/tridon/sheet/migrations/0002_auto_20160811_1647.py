# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheetfile',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Uploaded'),
        ),
    ]
