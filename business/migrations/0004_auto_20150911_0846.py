# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_geoentity_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeoEntity',
            new_name='Location',
        ),
    ]
