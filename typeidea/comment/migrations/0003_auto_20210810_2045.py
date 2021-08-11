# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-10 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20210808_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=0, verbose_name='状态'),
        ),
    ]
