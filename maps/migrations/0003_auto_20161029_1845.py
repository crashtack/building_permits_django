# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20161028_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='master_use_permit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Master Use Permit'),
        ),
    ]