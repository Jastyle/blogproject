# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date article create'),
            preserve_default=False,
        ),
    ]