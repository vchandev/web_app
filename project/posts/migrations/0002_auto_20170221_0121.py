# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
