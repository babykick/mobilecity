# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_auto_20150803_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recommendItem',
            field=models.ForeignKey(related_name='comments', verbose_name=b'recommend item', to='recommendation.RecommendItem', null=True),
        ),
    ]
