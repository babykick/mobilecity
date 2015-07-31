# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_author_user'),
        ('recommendation', '0009_remove_recommenditem_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommenditem',
            name='author',
            field=models.ForeignKey(related_name='recommendations', default=None, verbose_name=b'author for the recommendation', to='users.Author'),
        ),
    ]
