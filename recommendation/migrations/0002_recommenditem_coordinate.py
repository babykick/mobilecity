# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='coordinate',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]