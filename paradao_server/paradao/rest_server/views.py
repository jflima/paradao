from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from models import Parada
# from sensor.models import Sensor
from sensor.models import SensorValue
from sensor.views import parseSensorsData
from serializers import ParadaSerializer
from serializers import SensorValueSerializer
from datetime import datetime, timedelta


# Create your views here.
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
