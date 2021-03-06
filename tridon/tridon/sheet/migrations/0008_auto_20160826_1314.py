# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0007_workbookentry_workbook_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbookentry',
            name='amount',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Amount incl. VAT'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='consignee_suburb',
            field=models.CharField(max_length=255, verbose_name='Consignee suburb'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='doc_fee',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Document Fee'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='fuel_surcharge',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Fuel Surchare Ex. Vat'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='kgs_used',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Kgs Used'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='min_charge',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Minimum Charge'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='rate_per_kg',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Rate Per Kg'),
        ),
        migrations.AlterField(
            model_name='workbookentry',
            name='return_no',
            field=models.IntegerField(verbose_name='Return No'),
        ),
    ]
