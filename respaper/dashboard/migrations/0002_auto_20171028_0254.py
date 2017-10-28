# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='abstract',
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_name',
            field=models.CharField(default='paper name', max_length=200),
        ),
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(),
        ),
    ]