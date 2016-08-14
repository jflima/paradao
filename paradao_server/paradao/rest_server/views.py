from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from models import Parada
from models import StatusParada
# from sensor.models import Sensor
from sensor.models import SensorValue
from sensor.views import parseSensorsData
from serializers import ParadaSerializer
from serializers import StatusParadaSerializer
from serializers import SensorValueSerializer
from datetime import datetime, timedelta


# Create your views here.
def calcular_conceito(status):
    total = status.temperatura + status.luminosidade + \
        status.umidade + status.presenca

    media = total / 4

    if media > 1:
        return 1
    else:
        return 0


def processar_sensores(valores):
    umidade = valores.get(sensor__nome="UT_01 - Umidade")
    temperatura = valores.get(sensor__nome="UT_01 - Temperatura")
    luminosidade = valores.get(sensor__nome="LDR_01")
    presenca = valores.get(sensor__nome="PIR_01")

    status = StatusParada()

    status.valor_temperatura = temperatura.valor
    if temperatura < 18:
        status.temperatura = 0
    elif 18 < temperatura < 28:
        status.temperatura = 1
    else:
        status.temperatura = 2

    if luminosidade < 200:
        status.luminosidade = 0
    elif 200 < luminosidade < 800:
        status.luminosidade = 1
    else:
        status.luminosidade = 2

    if umidade < 30:
        status.umidade = 0
    elif umidade > 80:
        status.umidade = 1
    else:
        status.umidade = 2

    status.presenca = presenca.valor

    status.conceito_parada = calcular_conceito(status)

    return status


@api_view(['GET'])
@permission_classes((AllowAny,))
def parada_detail(request, pk, format=None):
    parada = Parada.objects.filter(codigo=pk).get()
    serializer = ParadaSerializer(parada, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
def leitura_sensores_parada(request, codigo_parada, format=None):
    parseSensorsData()
    valores = SensorValue.objects.filter(
        sensor__parada__codigo=codigo_parada,
        timestamp__gte=(datetime.now() - timedelta(seconds=5)))
    serializer = SensorValueSerializer(valores,
                                       context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
def status_parada(request, codigo_parada, format=None):
    parseSensorsData()
    valores = SensorValue.objects.filter(
        sensor__parada__codigo=codigo_parada,
        timestamp__gte=(datetime.now() - timedelta(seconds=5)))
    status_parada = processar_sensores(valores)
    status_parada.parada = Parada.objects.get(codigo=codigo_parada)
    serializer = StatusParadaSerializer(status_parada,
                                        context={'request': request}, many=False)
    return Response(serializer.data)
