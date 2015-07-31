# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0011_auto_20150731_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommenditem',
            name='author',
            field=models.ForeignKey(related_name='recommendations', verbose_name=b'author for the recommendation', to='users.Author', null=True),
        ),
    ]
