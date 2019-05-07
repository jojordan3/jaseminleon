# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('contact', '0006_auto_20170907_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='feed_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
