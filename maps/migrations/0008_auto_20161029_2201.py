# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20161029_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='contractor',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Contractor'),
        ),
    ]