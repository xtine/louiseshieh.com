# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe

from .models import AboutPage, Project


admin.site.site_title = "Louise Shieh Admin"
admin.site.site_header = "Louise Shieh"
admin.site.index_title = "Site Administration"

admin.site.register(AboutPage)

class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'home_page_image', 'home_page_image_preview', 'featured_image', 'featured_image_preview', 'home_page_order')
    readonly_fields = ('home_page_image_preview', 'featured_image_preview')
    list_display = ('title', 'home_page_list_image', 'home_page_order')

    ordering = ('home_page_order',)

    def home_page_list_image(self, obj):
        return mark_safe(
            """<img src="%s%s" style="max-width: 150px" />"""
            % (settings.MEDIA_URL, obj.home_page_image))

admin.site.register(Project, ProjectAdmin)
