# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0012_auto_20150804_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='category',
            field=models.CharField(max_length=20, null=True, choices=[(b'WESTFOOD', '\u897f\u9910'), (b'CHINESEFOOD', '\u4e2d\u9910')]),
        ),
    ]
