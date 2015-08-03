# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_auto_20150803_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommenditem',
            options={'ordering': ['-publishTime']},
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
