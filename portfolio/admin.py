# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe

from .models import AboutPage, Project, ProjectMedia


# General Admin setup
admin.site.site_title = "Louise Shieh Admin"
admin.site.site_header = "Louise Shieh"
admin.site.index_title = "Site Administration"

# Admin for About page
admin.site.register(AboutPage)

# Admin for Project media rows
class ProjectMediaInline(admin.StackedInline):
    model = ProjectMedia
    fields = ['image', 'image_preview', 'video', 'copy']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                """<img src="%s%s" style="max-width: 800px" />"""
                % (settings.MEDIA_URL, obj.image))
        else:
            return ""


# Admin for Projects
class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'home_page_image', 'home_page_image_preview', 'home_page_order')
    readonly_fields = ('home_page_image_preview',)
    list_display = ('title', 'home_page_list_image', 'home_page_order')
    inlines = (ProjectMediaInline,)

    ordering = ('home_page_order',)

    def home_page_list_image(self, obj):
        return mark_safe(
            """<img src="%s%s" style="max-width: 150px" />"""
            % (settings.MEDIA_URL, obj.home_page_image))

admin.site.register(Project, ProjectAdmin)
