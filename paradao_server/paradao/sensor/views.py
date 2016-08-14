# from django.shortcuts   import get_object_or_404
from django.shortcuts   import render
# from django.http        import HttpResponseRedirect
# from django.views       import generic
from .models            import Sensor, SensorValue
# from rest_server.models import Parada
import json
import urllib2


# Create your views here.
def parseSensorsData():
    #jsonStr = urllib2.urlopen('http://hackercidadao.com.br/embarquelab/downloads/EL_sensores_json.php')
    jsonStr = urllib2.urlopen('http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php')
    sensorsDict = json.loads(jsonStr.read())
    sensor_values = []
    for sensor in sensorsDict['Sensor']:
        sen = Sensor.objects.filter(codigo=int(sensor['Codigo']))
        if(sen):
            sen = sen.get()
            val = SensorValue(sensor=sen, valor=sensor['Valor'])
            val.save()
            sensor_values.append(val)
    return sensor_values


def sensorList(request):
    parseSensorsData(request)
    context = {
    }
    return render(request, 'sensor/sensorList.html', context)


def leitura_parada(request, parada):
    SensorValue.objects.filter(sensor__parada=parada).order_by('timestamp')
