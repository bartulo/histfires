# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170621_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='mdt',
            field=models.ImageField(upload_to=web.models.site_path),
        ),
        migrations.AlterField(
            model_name='site',
            name='pnoa',
            field=models.FileField(upload_to='static'),
        ),
    ]
