# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0009_auto_20150803_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': 'publishTime'},
        ),
        migrations.AlterModelOptions(
            name='recommenditem',
            options={'get_latest_by': 'publishTime'},
        ),
    ]
