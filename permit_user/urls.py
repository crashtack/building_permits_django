from django.conf.urls import url
from . import views
from views import EditUserLocationView, test_form_fill
# from models import PermitUser


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$',
        test_form_fill,
        name="test_form_fill"),
    url(r'^edit/$',
        EditUserLocationView.as_view(),
        name='edit_user_location'
        )
]
