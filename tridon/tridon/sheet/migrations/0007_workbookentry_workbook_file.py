# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0006_auto_20160815_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='workbookentry',
            name='workbook_file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sheet.WorkbookFile'),
            preserve_default=False,
        ),
    ]
