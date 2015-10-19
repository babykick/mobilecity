# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_auto_20151019_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='title',
            field=models.CharField(max_length=500, verbose_name='\u6807\u9898'),
        ),
    ]
