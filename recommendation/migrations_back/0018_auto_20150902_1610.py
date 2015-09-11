# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0017_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='publishTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
