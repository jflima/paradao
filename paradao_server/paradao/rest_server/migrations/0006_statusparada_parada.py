# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_server', '0005_statusparada'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusparada',
            name='parada',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rest_server.Parada'),
            preserve_default=False,
        ),
    ]