# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Project, AboutPage


def home(request):
    projects = Project.objects.order_by('home_page_order')
    page_name = 'home'

    return render(request, 'index.html', {
        'projects': projects,
        'page': page_name
    })

def about(request):
    about = AboutPage.objects.first()
    page_name = 'about'

    return render(request, 'about.html', {
        'about': about,
        'page': page_name
    })
