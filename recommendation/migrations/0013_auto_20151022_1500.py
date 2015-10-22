# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0012_recommenditem_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='uid',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
