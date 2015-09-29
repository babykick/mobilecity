# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_poi_city'),
        ('users', '0007_author_hometown'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('publishTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('upCount', models.IntegerField(default=0)),
                ('downCount', models.IntegerField(default=0)),
                ('author', models.ForeignKey(related_name='comments', default=1, verbose_name=b'comment author', to='users.Author', null=True)),
            ],
            options={
                'ordering': ['publishTime'],
                'get_latest_by': 'publishTime',
            },
        ),
        migrations.CreateModel(
            name='RecommendItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('summary', models.CharField(default=b'', max_length=500, blank=True)),
                ('content', models.CharField(default=b'', max_length=1000)),
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
                ('category', models.CharField(blank=True, max_length=20, null=True, choices=[('\u7f8e\u98df', '\u7f8e\u98df'), ('\u670d\u88c5', '\u670d\u88c5'), ('\u6570\u7801', '\u6570\u7801'), ('\u56fe\u4e66', '\u56fe\u4e66')])),
                ('publishTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('upCount', models.IntegerField(default=0)),
                ('downCount', models.IntegerField(default=0)),
                ('author', models.ForeignKey(related_name='recommendations', default=1, verbose_name=b'author for the recommendation', to='users.Author', null=True)),
                ('location', models.OneToOneField(null=True, blank=True, to='business.Location')),
            ],
            options={
                'get_latest_by': 'publishTime',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('recommendItem', models.ForeignKey(related_name='tags', verbose_name=b'recommend item', to='recommendation.RecommendItem', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='recommendItem',
            field=models.ForeignKey(related_name='comments', verbose_name=b'recommend item', to='recommendation.RecommendItem', null=True),
        ),
    ]
