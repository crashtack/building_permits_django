import os
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2


def index(request):
    return HttpResponse("Hello, world")


class MapView(DetailView):
    """
    Shows a Map and with plotted points.
    """
    model = User
    template_name = 'maps/map.html'

    def get_point(url):
        point = GeoIP2()
        return point.lat_lon(url)

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['googleapikey'] = os.environ.get('GOOGLE_MAPS_API_KEY')
        point = MapView.get_point(
            'ec2-35-160-27-154.us-west-2.compute.amazonaws.com'
        )
        context['data'] = [{'lat': point[0], 'lng': point[1]}, ]
        # import pdb; pdb.set_trace()
        return context
