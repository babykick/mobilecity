# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_poi_city'),
        ('recommendation', '0003_remove_recommenditem_bduid'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='poi',
            field=models.ForeignKey(related_name='recommendations', to='business.POI', null=True),
        ),
    ]
