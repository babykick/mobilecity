# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_location_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lon', models.FloatField(default=0)),
                ('lat', models.FloatField(default=0)),
                ('description', models.CharField(max_length=200, null=True)),
                ('vote_num', models.IntegerField(default=0)),
                ('visited_freq', models.IntegerField(default=0)),
                ('bdpoi_id', models.CharField(max_length=25, unique=True, null=True)),
            ],
        ),
    ]
