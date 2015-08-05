# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_author_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
