# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='r_call_phone',
            field=models.CharField(max_length=50),
        ),
    ]
