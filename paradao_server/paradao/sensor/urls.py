from django.conf.urls import url

from . import views

urlpatterns = [
    # /sensorList
    url(r'^$', views.sensorList, name='sensorList'),
]
