# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from .models import Project, AboutPage


def home(request):
    projects = Project.objects.order_by('home_page_order')
    page_name = 'home'

    return render(request, 'index.html', {
        'projects': projects,
        'page': page_name
    })


def project(request, name):
    name = name.replace('-', ' ')
    project = get_object_or_404(Project, title__iexact=name)

    return render(request, 'project.html', {
        'project': project
    })


def about(request):
    about = AboutPage.objects.first()
    page_name = 'about'

    return render(request, 'about.html', {
        'about': about,
        'page': page_name
    })


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
