# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_moviemodel_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMovieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_seat', models.IntegerField()),
            ],
        ),
    ]
