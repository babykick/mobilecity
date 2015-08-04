# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20150803_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoentity',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
