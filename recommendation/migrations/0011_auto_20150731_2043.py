# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0010_recommenditem_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='collectStatus',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='comment',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='interestedStatus',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='isLarge',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='likeStatus',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='picList',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='picListString',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='picOne',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='picThr',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='picTwo',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='readStatus',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='summary',
            field=models.CharField(default=b'', max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='recommenditem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
