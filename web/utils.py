import os
from django.core.files import File
from osgeo import gdal
from django.conf import settings

def get_coordinates(point):
     n = point.geom.y + point.extension/2
     s = point.geom.y - point.extension/2
     e = point.geom.x + point.extension/2
     w = point.geom.x - point.extension/2
     return (w,n,e,s)

def save_to_folder(inst, n):
    carpeta = os.path.join(settings.BASE_DIR, "static")
    coord = get_coordinates(inst)
    if n == 'mdt':
        ext = 'bin'
    elif n == 'pnoa':
        ext = 'jpg'
    img = os.path.join(carpeta, '%s.%s' % (n, ext))
    xml = gdal.Open(os.path.join(carpeta, 'xml/%s.xml' % n))
    if n == 'mdt':
        xml = gdal.Translate(img, xml, projWin = coord) 
    elif n == 'pnoa':
        xml = gdal.Translate(img, xml, projWin = coord, format = 'JPEG') 
    xml = None
    f = open(img)
    if n == 'mdt':
        inst.mdt.save('%s.%s' % (n, ext), File(f), save=False)
    elif n == 'pnoa':
        inst.pnoa.save('%s.%s' % (n, ext), File(f), save=False)
    os.remove(img) 
