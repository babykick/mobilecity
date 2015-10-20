# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0009_auto_20151019_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='cloudImage',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'cloud_image', blank=True),
        ),
    ]
