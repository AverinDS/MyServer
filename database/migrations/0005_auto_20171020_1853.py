# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20171013_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='shopFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Shop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shopFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Shop'),
        ),
    ]