# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0004_auto_20171208_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='family',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='备注'),
        ),
    ]
