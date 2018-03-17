# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-17 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('body', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'About Page',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('home_page_image', models.ImageField(upload_to='media/')),
                ('featured_image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
