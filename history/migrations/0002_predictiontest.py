# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('symbol', models.CharField(max_length=30)),
                ('percent_correct', models.FloatField()),
                ('avg_diff', models.FloatField()),
                ('datasetinputs', models.IntegerField()),
                ('hiddenneurons', models.IntegerField()),
                ('granularity', models.IntegerField()),
                ('output', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
