# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-03 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20170120_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymoustarget',
            name='mail_sent_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
