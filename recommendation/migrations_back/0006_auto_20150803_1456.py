# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_auto_20150803_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='publishTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
