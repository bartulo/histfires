# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})

def visor(request, site_id):
    site = Site.objects.get(pk=site_id)
    return render(request, 'visor.html', {'site': site})
