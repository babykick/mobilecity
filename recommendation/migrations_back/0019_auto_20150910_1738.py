# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0018_auto_20150902_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommenditem',
            old_name='geo',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[('\u7f8e\u98df', '\u7f8e\u98df'), ('\u670d\u88c5', '\u670d\u88c5'), ('\u6570\u7801', '\u6570\u7801'), ('\u56fe\u4e66', '\u56fe\u4e66')]),
        ),
    ]
