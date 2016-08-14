from django.conf.urls import url, include
from models import Parada
from sensor.models import Sensor
from rest_framework import routers, viewsets
from serializers import ParadaSerializer
from serializers import SensorSerializer
from . import views


# ViewSets define the view behavior.
class ParadaViewSet(viewsets.ModelViewSet):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'parada', ParadaViewSet)
router.register(r'sensor', SensorViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^parada/(?P<pk>[0-9]+)$', views.parada_detail),
    url(r'^parada/(?P<codigo_parada>[0-9]+)/sensores$', views.leitura_sensores_parada),
]
