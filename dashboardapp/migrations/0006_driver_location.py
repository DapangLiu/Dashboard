# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-28 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0005_auto_20161227_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
