# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_auto_20150731_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommenditem',
            name='author',
        ),
    ]
