from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from permit_user.models import PermitUser
from django.urls import reverse_lazy
from django import forms


def index(request):
    return HttpResponse("Hello, world")


@login_required
def test_form_fill(request):
    """
    Testing the Geolocation form fill feature of jquery.geocomplete.js
    source: https://ubilabs.github.io/geocomplete/
    """
    context = {'form': 1}
    return render(request, 'test_form_fill.html', context)


@method_decorator(login_required, name='dispatch')
class EditUserLocationView(UpdateView):
    """
    Edit the PermitUsers current location based no the the search
    address they enter
    """
    model = User
    # form_class = NameForm
    # fields = [
    #     'latitude',
    #     'longitude',
    #     'location',
    # ]
    fields = ['first_name', 'last_name', 'email']
    template_name = 'update_user_location.html'
    success_url = reverse_lazy('form')

    def get_object(self):
        return self.request.user

    def get_form(self, *args, **kwargs):
        form = super(EditUserLocationView, self).get_form(*args, **kwargs)

        form.fields['latitude'] = forms.fields.FloatField(
            initial=self.object.permituser.latitude
        )

        form.fields['longitude'] = forms.fields.FloatField(
            initial=self.object.permituser.longitude
        )

        form.fields['location'] = forms.fields.CharField(
            initial=self.object.permituser.location
        )

        return form

    def form_valid(self, form):
        """Update user location upon valid form"""
        form.instance.permituser.latitude = form.cleaned_data.get('latitude')
        form.instance.permituser.longitude = form.cleaned_data.get('longitude')
        form.instance.permituser.location = form.cleaned_data.get('location')
        form.instance.permituser.save()
        return super(EditUserLocationView, self).form_valid(form)
