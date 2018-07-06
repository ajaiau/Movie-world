# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_remove_moviemodel_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/Images/'),
            preserve_default=False,
        ),
    ]