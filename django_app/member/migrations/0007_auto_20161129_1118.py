# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20161129_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]