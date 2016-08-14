from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^',            include("rest_server.urls")),
    url(r'^web',         include("web.urls")),
    url(r'^sensor_list', include("sensor.urls")),
    url(r'^admin/',      include(admin.site.urls)),
]
