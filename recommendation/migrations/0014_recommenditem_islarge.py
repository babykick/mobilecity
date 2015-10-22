# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0013_auto_20151022_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='isLarge',
            field=models.BooleanField(default=False),
        ),
    ]
