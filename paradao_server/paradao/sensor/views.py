from django.shortcuts import render
from django.http import HttpResponse
import json, urllib2

# Create your views here.
def sensorParser(request):
    jsonStr = urllib2.urlopen('http://hackercidadao.com.br/embarquelab/downloads/EL_sensores_json.php')
    sensorsDict = json.loads(jsonStr.read())
    context = {
        'sensorList' : sensorsDict['Sensor'],
        'sensorsQtt' : len(sensorsDict['Sensor']),
    }

    return render(request, 'sensor/sensorList.html', context)


