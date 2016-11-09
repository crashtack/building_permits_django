import os
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2
from maps.models import Permit
from django.shortcuts import render
from maps.forms import NameForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
import sys
sys.path.append(os.path.join(os.environ.get('PWD', ''), 'permit_user'))
from permit_user.models import PermitUser


def index(request):
    return HttpResponse("Hello, world")


def user_location(request):
    """ View for the test map"""
    context = {'name': 'fred'}
    context['googleapikey'] = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render(request, 'maps/noisy.html', context)


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

        points = []
        for pp in Permit.objects.all():
            points.append({
                'lat': pp.latitude,
                'lng': pp.longitude,
                'num': pp.permit_number,
                'description': pp.description,
            })

        context['data'] = points
        # import pdb; pdb.set_trace()
        return context


class TestMapView(DetailView):
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


class FormTestView(FormView):
    template_name = 'form.html'
    form_class = NameForm
    success_url = reverse_lazy('form')
    name = ''

    def form_valid(self, form):
        self.name = form.cleaned_data['location']
        form.send_email()
        return super(FormTestView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FormTestView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context['name'] = self.name
        return context


@method_decorator(login_required, name='dispatch')
class EditUserLocationView(UpdateView):
    """
    Edit the PermitUsers current location based no the the search
    address they enter
    """
    model = PermitUser
    # form_class = NameForm
    fields = [
        'bio',
        'latitude',
        'longitude',
        'location',
    ]
    template_name = 'form.html'
    success_url = reverse_lazy('form')

    # def get_object(self):
    #     self.user = self.request.user.permituser
    #     return self.user
    #
    # def get_context_data(self, **kwargs):
    #     context = super(EditUserLocationView, self).get_context_data(**kwargs)
    #     # import pdb; pdb.set_trace()
    #     context['user'] = self.user
    #     return context
    #
    # def get_form(self, *args, **kwargs):
    #     form = super(EditUserLocationView, self).get_form(*args, **kwargs)
    #     # form.fields['bio'] = form.fields.CharField(initial=self.user.permituser.bio)
    #     form.fields['bio'] = form.fields.CharField(initial="yo")
    #     return form

    # def get_form_kwargs(self):
    #     kwargs = super(EditUserLocationView, self).get_form_kwargs()
    #     kwargs.update({'permituser': self.request.user})
    #     return kwargs
