# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Parada(models.Model):
    codigo = models.TextField(default='', help_text="Codigo da parada")
    logradouro = models.TextField(default='', help_text="Logradouro da parada")
    bairro = models.TextField(default='', help_text="Bairro da parada")
    cidade = models.TextField(default='', help_text="Cidade da parada")
    latitude = models.TextField(default='', help_text="Latitude da parada")
    longitude = models.TextField(default='', help_text="Longitude da parada")
