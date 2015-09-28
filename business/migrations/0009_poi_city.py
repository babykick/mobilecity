# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20150924_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='city',
            field=models.CharField(default='\u5cb3\u9633', max_length=20),
            preserve_default=False,
        ),
    ]
