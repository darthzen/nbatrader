# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0003_auto_20170713_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(upload_to=b'logos/'),
        ),
    ]
