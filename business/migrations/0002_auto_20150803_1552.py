# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField(default=0)),
                ('lat', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='basestation',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='basestation',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='lon',
        ),
        migrations.AddField(
            model_name='basestation',
            name='geo',
            field=models.OneToOneField(null=True, to='business.GeoEntity'),
        ),
        migrations.AddField(
            model_name='shop',
            name='geo',
            field=models.OneToOneField(null=True, to='business.GeoEntity'),
        ),
    ]
