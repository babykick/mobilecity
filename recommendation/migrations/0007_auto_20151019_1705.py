# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0006_auto_20151019_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='poi',
            field=models.ForeignKey(related_name='recommendations', blank=True, to='business.POI', null=True),
        ),
    ]
