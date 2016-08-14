from django.shortcuts   import get_object_or_404, render
from django.http        import HttpResponseRedirect
from django.views       import generic
from .models            import Sensor, SensorValue
from rest_server.models import Parada
import json, urllib2

# Create your views here.
def sensorList(request):
        jsonStr = urllib2.urlopen('http://hackercidadao.com.br/embarquelab/downloads/EL_sensores_json.php')
        sensorsDict = json.loads(jsonStr.read())
        for sensor in sensorsDict['Sensor']:
            sen = Sensor.objects.filter(codigo=int(sensor['Codigo'])).get()
            val = SensorValue(sensor=sen, valor=sensor['Valor'])
            val.save()
        
        context = {
            'sensorList' : sensorsDict['Sensor'],
            'sensorsQtt' : len(sensorsDict['Sensor']),
        }
        return render(request, 'sensor/sensorList.html', context)

