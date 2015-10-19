# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_auto_20151019_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='cloud_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'image'),
        ),
    ]
