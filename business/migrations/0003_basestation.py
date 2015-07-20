# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_delete_basestation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('height', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
