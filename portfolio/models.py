# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    home_page_image = models.ImageField(upload_to='project/', blank=False)
    home_page_order = models.IntegerField(blank=False)

    def home_page_image_preview(self):
        if self.home_page_image:
            return mark_safe("""<img src="%s%s" />""" % (settings.MEDIA_URL, self.home_page_image))
        else:
            return ""

    home_page_image_preview.short_description = 'Home page image preview'
    home_page_image_preview.allow_tags = True

    def __str__(self):
        return self.title


class ProjectMedia(models.Model):
    project = models.ForeignKey('Project')
    image = models.ImageField(upload_to='project/', blank=True, help_text='Uploading an image will override the video embed.')
    video = models.CharField(max_length=100, blank=True, help_text='Vimeo ID.<br>Example: ID is 123 if url is https://www.vimeo.com/123')
    copy = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Project Media'

    def __str__(self):
        return self.project.title


class AboutPage(models.Model):
    image = models.ImageField(upload_to='about/', blank=True)
    body = models.TextField(blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe("""<img src="%s%s" />""" % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_preview.short_description = 'Image preview'
    image_preview.allow_tags = True

    class Meta:
        verbose_name_plural = 'About Page'

    def __str__(self):
        return 'About Page'

