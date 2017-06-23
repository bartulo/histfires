from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView

from . import views
from .models import Site

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<site_id>[0-9]+)/$', views.visor, name='visor'),
    url(r'^data.geojson', GeoJSONLayerView.as_view(model=Site), name='data'),
]
