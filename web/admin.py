# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from .models import *

class SiteAdmin(admin.OSMGeoAdmin):
  exclude = ('mdt', 'pnoa')
  list_display = ('nombre', 'extension')
  default_lon = -420709
  default_lat = 4882227
  default_zoom = 5


admin.site.register(Site, SiteAdmin)
