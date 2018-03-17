# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Project, AboutPage


def home(request):
    projects = Project.objects.order_by('home_page_order')

    return render(request, 'index.html', {
        'projects': projects
    })
