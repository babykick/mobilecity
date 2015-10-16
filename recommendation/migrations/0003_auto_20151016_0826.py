# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('recommendation', '0002_recommenditem_coordinate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recommendItem',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='recommendItem',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
