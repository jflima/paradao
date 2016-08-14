# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Sensor(models.Model):
    codigo = models.IntegerField(default=0, help_text="Codigo do sensor")
    porta = models.IntegerField(default=0, help_text="Porta do sensor")
    nome = models.TextField(default='', help_text="Nome do sensor")
    descricao = models.TextField(default='', help_text="Descricao do sensor")
    localizacao = models.TextField(default='',
                                   help_text="Localizacao do sensor")
    tipo = models.TextField(default='', help_text="Tipo do sensor")
    data_sheet = models.TextField(default='', help_text="Data sheet do sensor")
    minimo = models.IntegerField(default=0, help_text="Minimo do sensor")
    maximo = models.IntegerField(default=0, help_text="Maximo do sensor")
    valor = models.FloatField(default=0.0, help_text="Valor do sensor")
