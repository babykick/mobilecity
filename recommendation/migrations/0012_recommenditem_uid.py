# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0011_auto_20151020_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='uid',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
