# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_author_isadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isDeveloper',
            field=models.BooleanField(default=False),
        ),
    ]
