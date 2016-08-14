from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from models import Parada
from sensor.models import Sensor
from serializers import ParadaSerializer
from serializers import SensorSerializer


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
    sensores = Sensor.objects.filter(parada__codigo=codigo_parada)
    serializer = ParadaSerializer(sensores, many=True)
    return Response(serializer.data)
