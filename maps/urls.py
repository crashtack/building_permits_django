from django.conf.urls import url
from maps.views import MapView, user_location
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/$',
        user_location,
        name='user_location'),
    url(
        r'^map/(?P<pk>[0-9]+)$',
        MapView.as_view(),
        name='map'
    ),

]
