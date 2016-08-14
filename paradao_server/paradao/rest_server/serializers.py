from rest_framework import serializers
from models import Parada
from sensor.models import Sensor
from sensor.models import SensorValue


# Serializers define the API representation.
class ParadaSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = Parada
				fields = ('codigo', 'logradouro', 'bairro',
									'cidade', 'latitude', 'longitude')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = Sensor
				fields = ('codigo', 'porta', 'nome',
									'descricao', 'localizacao', 'tipo',
									'data_sheet', 'minimo', 'maximo', 'valor',
									'parada')


class SensorValueSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = SensorValue
				fields = ('sensor', 'valor', 'timestamp')
