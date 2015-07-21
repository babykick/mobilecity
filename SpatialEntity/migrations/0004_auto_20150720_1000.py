# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_basestation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basestation',
            old_name='name',
            new_name='site_name',
        ),
        migrations.RemoveField(
            model_name='basestation',
            name='height',
        ),
        migrations.AddField(
            model_name='basestation',
            name='cluster',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
