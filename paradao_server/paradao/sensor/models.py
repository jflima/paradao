# -*- coding: utf-8 -*-
from django.db import models
from rest_server.models import Parada


# Create your models here.

class Sensor(models.Model):
    parada = models.ForeignKey(Parada)
    codigo = models.IntegerField(primary_key=True, default=0, help_text="Codigo do sensor")
    porta = models.IntegerField(default=0, help_text="Porta do sensor")
    nome = models.TextField(default='', help_text="Nome do sensor")
    descricao = models.TextField(default='', help_text="Descricao do sensor")
    localizacao = models.TextField(default='',
                                   help_text="Localizacao do sensor")
    tipo = models.TextField(default='', help_text="Tipo do sensor")
    data_sheet = models.TextField(default='', help_text="Data sheet do sensor")
    minimo = models.IntegerField(default=0, help_text="Minimo do sensor")
    maximo = models.IntegerField(default=0, help_text="Maximo do sensor")

    def __str__(self):
        return "Codigo:%d,Nome: %s, Tipo: %s, Porta:%d, Localizacao:%s" % (self.codigo, self.nome, self.tipo, self.porta, self.localizacao)


class SensorValue(models.Model):
    sensor = models.ForeignKey(Sensor)
    valor  = models.FloatField(default=0.0, help_text="Valor do sensor")
    timestamp = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return "[Sensor:%d]@[time %s]=%d"%(self.sensor.codigo, str(self).timestamp, self.valor)

