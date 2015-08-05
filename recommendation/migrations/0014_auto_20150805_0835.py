# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0013_recommenditem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recommenditem',
            name='downCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recommenditem',
            name='upCount',
            field=models.IntegerField(default=0),
        ),
    ]
