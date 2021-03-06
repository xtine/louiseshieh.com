# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180324_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmedia',
            options={'verbose_name_plural': 'Project Media'},
        ),
        migrations.AlterField(
            model_name='projectmedia',
            name='image',
            field=models.ImageField(blank=True, help_text='Uploading an image will override the video embed.', upload_to='project/'),
        ),
        migrations.AlterField(
            model_name='projectmedia',
            name='video',
            field=models.CharField(blank=True, help_text='Vimeo ID.', max_length=100),
        ),
    ]
