# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_auto_20150728_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='content',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='summary',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
