from django.conf.urls import url
from map.views import MapView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^map$',
        MapView.as_view(),
        name='map'
    ),

]
