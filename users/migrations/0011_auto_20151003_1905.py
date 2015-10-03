# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20151002_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='userAuth',
            new_name='user',
        ),
    ]
