# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-10 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.TextField(blank=True, help_text='如果设置的不是HTML类型，可为空', max_length=500, verbose_name='内容'),
        ),
    ]