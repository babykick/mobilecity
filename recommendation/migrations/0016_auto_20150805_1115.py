# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0015_auto_20150805_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='category',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
