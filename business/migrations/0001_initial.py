# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('geomodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='business.GeoModel')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            bases=('business.geomodel',),
        ),
    ]
