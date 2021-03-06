# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_server', '0003_auto_20160814_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0, help_text=b'Codigo do sensor')),
                ('porta', models.IntegerField(default=0, help_text=b'Porta do sensor')),
                ('nome', models.TextField(default=b'', help_text=b'Nome do sensor')),
                ('descricao', models.TextField(default=b'', help_text=b'Descricao do sensor')),
                ('localizacao', models.TextField(default=b'', help_text=b'Localizacao do sensor')),
                ('tipo', models.TextField(default=b'', help_text=b'Tipo do sensor')),
                ('data_sheet', models.TextField(default=b'', help_text=b'Data sheet do sensor')),
                ('minimo', models.IntegerField(default=0, help_text=b'Minimo do sensor')),
                ('maximo', models.IntegerField(default=0, help_text=b'Maximo do sensor')),
                ('valor', models.FloatField(default=0.0, help_text=b'Valor do sensor')),
                ('parada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_server.Parada')),
            ],
        ),
    ]
