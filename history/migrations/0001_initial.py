# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('symbol', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
