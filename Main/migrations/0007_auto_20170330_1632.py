# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-30 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20170330_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='key',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='target',
            name='mail_address',
            field=models.EmailField(max_length=254),
        ),
    ]
