# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0017_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='tube.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='VtubeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.DeleteModel(
            name='VtubeMerch',
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.Video'),
        ),
    ]