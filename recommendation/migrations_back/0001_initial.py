# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(default=b'', max_length=500, blank=True)),
                ('content', models.CharField(default=b'', max_length=1000)),
                ('comment', models.CharField(default=b'', max_length=100, blank=True)),
                ('picListString', models.CharField(default=b'', max_length=100, blank=True)),
                ('picOne', models.CharField(default=b'', max_length=100, blank=True)),
                ('picTwo', models.CharField(default=b'', max_length=100, blank=True)),
                ('picThr', models.CharField(default=b'', max_length=100, blank=True)),
                ('picList', models.CharField(default=b'', max_length=100, blank=True)),
                ('isLarge', models.CharField(default=b'', max_length=100, blank=True)),
                ('readStatus', models.CharField(default=b'', max_length=100, blank=True)),
                ('collectStatus', models.CharField(default=b'', max_length=50, blank=True)),
                ('likeStatus', models.CharField(default=b'', max_length=50, blank=True)),
                ('interestedStatus', models.CharField(default=b'', max_length=50, blank=True)),
                ('author', models.ForeignKey(related_name='recommendations', verbose_name=b'author for the recommendation', to='users.Author', null=True)),
            ],
        ),
    ]
