# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-26 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0012_auto_20190126_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tube.Video'),
        ),
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
