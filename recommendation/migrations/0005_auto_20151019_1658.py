# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_recommenditem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommenditem',
            name='image',
        ),
        migrations.AddField(
            model_name='recommenditem',
            name='mainImage',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'main_image', blank=True),
        ),
    ]
