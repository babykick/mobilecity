# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_author_islocal'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='hometown',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
