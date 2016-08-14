# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Parada(models.Model):
    codigo = models.TextField(primary_key=True, default='', help_text="Codigo da parada")
    logradouro = models.TextField(default='', help_text="Logradouro da parada")
    bairro = models.TextField(default='', help_text="Bairro da parada")
    cidade = models.TextField(default='', help_text="Cidade da parada")
    latitude = models.TextField(default='', help_text="Latitude da parada")
    longitude = models.TextField(default='', help_text="Longitude da parada")

    def __str__(self):
        return "Parada[%s]: latitude=%s longitude=%s"%(self.codigo, self.latitude, self.longitude)


class StatusParada(models.Model):
    parada = models.ForeignKey(Parada)
    valor_temperatura = models.FloatField(default=0.0)
    temperatura = models.IntegerField(default=0)
    umidade = models.IntegerField(default=0)
    luminosidade = models.IntegerField(default=0)
    presenca = models.IntegerField(default=0)
    conceito_parada = models.IntegerField(default=0)
