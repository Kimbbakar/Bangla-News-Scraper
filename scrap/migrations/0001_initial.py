# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-27 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('portal_name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=5000)),
                ('img', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]