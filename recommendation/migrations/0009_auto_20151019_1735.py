# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_recommenditem_cloud_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommenditem',
            name='cloud_image',
        ),
        migrations.RemoveField(
            model_name='recommenditem',
            name='mainImage',
        ),
        migrations.AddField(
            model_name='recommenditem',
            name='cloudImage',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'cloud_image'),
        ),
    ]
