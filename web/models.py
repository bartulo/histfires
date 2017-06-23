# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.conf import settings
from django.core.files import File
from osgeo import gdal
import os
from utils import get_coordinates, save_to_folder

def site_path(instance, filename):
    return 'static/images/site_%s/mdt.bin' % instance.nombre
def site_path_pnoa(instance, filename):
    return 'static/images/site_%s/pnoa.jpg' % instance.nombre

class Site(models.Model):
    nombre = models.CharField(max_length=100)
    extension = models.FloatField()
    mdt = models.ImageField(upload_to=site_path)
    pnoa = models.FileField(upload_to=site_path_pnoa)
    geom = models.PointField(srid=25830)

    def save(self, *args, **kwargs):
        save_to_folder(self, 'mdt')
        save_to_folder(self, 'pnoa')
        super(Site, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
