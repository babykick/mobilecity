# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20150803_1552'),
        ('recommendation', '0006_auto_20150803_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='geo',
            field=models.OneToOneField(null=True, to='business.GeoEntity'),
        ),
    ]
