# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_recommenditem_geo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='geo',
            field=models.OneToOneField(null=True, blank=True, to='business.GeoEntity'),
        ),
    ]
