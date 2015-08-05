# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_author_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
