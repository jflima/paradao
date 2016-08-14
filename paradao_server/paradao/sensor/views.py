from django.shortcuts import render
from django.http import HttpResponse
import json, urllib2

# Create your views here.
def sensorParser(request):
    jsonStr = urllib2.urlopen('http://hackercidadao.com.br/embarquelab/downloads/EL_sensores_json.php')
    dct = json.loads(jsonStr.read())
    response = '<html><body> <h1>#%d Sensores:</h1>'%(len(dct['Sensor']))

    for iterator in range(0, len(dct['Sensor'])):
        response = response + "<p>   * sensor[%d]= %s</p>" % (iterator, dct['Sensor'][iterator])
    response = response + "</body></html>"

    return HttpResponse(response)
