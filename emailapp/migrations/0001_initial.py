# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('confirmKey', models.CharField(blank=True, max_length=10, null=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
