# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('recommendation', '0003_auto_20150731_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='author',
            field=models.ForeignKey(related_name='recommendations', default=None, verbose_name=b'author for the recommendation', to='users.Author'),
        ),
    ]
