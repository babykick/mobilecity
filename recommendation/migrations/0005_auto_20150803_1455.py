# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_comment_recommenditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommenditem',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='publishTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recommenditem',
            name='publishTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
