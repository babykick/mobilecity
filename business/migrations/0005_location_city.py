# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20150911_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
