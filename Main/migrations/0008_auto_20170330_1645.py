# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-30 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_auto_20170330_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymoustarget',
            name='uniqueid',
            field=models.CharField(db_index=True, default=uuid.uuid4, max_length=36),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='key',
            field=models.CharField(db_index=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.CharField(db_index=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='target',
            name='mail_address',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]
