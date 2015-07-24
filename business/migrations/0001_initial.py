# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('site_name', models.CharField(max_length=100)),
                ('cluster', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
