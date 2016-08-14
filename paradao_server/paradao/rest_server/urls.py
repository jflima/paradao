from django.conf.urls import url, include
from models import Sensor
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('codigo', 'porta', 'nome',
                  'descricao', 'localizacao', 'tipo',
                  'data_sheet', 'minimo', 'maximo', 'valor')


# ViewSets define the view behavior.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
