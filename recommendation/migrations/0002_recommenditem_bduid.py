# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='bduid',
            field=models.CharField(max_length=25, unique=True, null=True),
        ),
    ]
