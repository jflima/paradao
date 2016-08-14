from django.shortcuts   import render
from .models            import Sensor, SensorValue
from rest_server.models import Parada
import json
import urllib2


# Create your views here.
def parseSensorsData(request):
        #jsonStr = urllib2.urlopen('http://hackercidadao.com.br/embarquelab/downloads/EL_sensores_json.php')
        jsonStr = urllib2.urlopen('http://172.19.5.253/embarquelab/downloads/EL_sensores_json.php')
        sensorsDict = json.loads(jsonStr.read())
        ret = False
        for sensor in sensorsDict['Sensor']:
            sen = Sensor.objects.filter(codigo=int(sensor['Codigo']))
            #sen = Sensor(codigo=sensor['Codigo'], porta=sensor['Porta'], nome=sensor['Nome'], descricao=sensor['Descricao'], localizacao=sensor['Localizacao'], tipo=sensor['Tipo'], data_sheet=sensor['DataSheet'], minimo=sensor['Minimo'], maximo=sensor['Maximo'], parada=Parada.objects.get(codigo="010001"))
            sen.save()
            if(sen):
                sen = sen.get()
                val = SensorValue(sensor=sen, valor=sensor['Valor'])
                val.save()
                ret = True
        return ret


def sensorList(request):
    success = parseSensorsData(request)
    context = {
            'success' : success,
    }
    return render(request, 'sensor/sensorList.html', context)


def leitura_parada(request, parada):
    SensorValue.objects.filter(sensor__parada=parada).order_by('timestamp')

