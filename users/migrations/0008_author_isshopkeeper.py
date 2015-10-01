# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_author_hometown'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isShopkeeper',
            field=models.BooleanField(default=False),
        ),
    ]
