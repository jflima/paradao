# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_server', '0004_auto_20160814_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusParada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_temperatura', models.FloatField(default=0.0)),
                ('temperatura', models.IntegerField(default=0)),
                ('umidade', models.IntegerField(default=0)),
                ('luminosidade', models.IntegerField(default=0)),
                ('presenca', models.IntegerField(default=0)),
                ('conceito_parada', models.IntegerField(default=0)),
            ],
        ),
    ]
