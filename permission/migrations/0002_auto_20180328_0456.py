# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='permissions',
            field=models.ManyToManyField(related_name='permissions', to='auth.Permission', verbose_name='Permissions'),
        ),
    ]
