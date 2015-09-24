# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_poi_coordinate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poi',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='lon',
        ),
    ]
