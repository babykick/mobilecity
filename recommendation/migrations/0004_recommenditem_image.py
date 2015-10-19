# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_auto_20151016_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'main_image'),
        ),
    ]
