# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0016_auto_20150805_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('recommendItem', models.ForeignKey(related_name='tags', verbose_name=b'recommend item', to='recommendation.RecommendItem', null=True)),
            ],
        ),
    ]
