# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20161111_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Course', verbose_name='course'),
        ),
    ]
