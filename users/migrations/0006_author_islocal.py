# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_author_isdeveloper'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isLocal',
            field=models.BooleanField(default=False),
        ),
    ]
