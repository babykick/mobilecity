#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem
from users.serializers import AuthorSerializer

class RcmdItemEntrySerializer(serializers.ModelSerializer):
    author = AuthorSerializer( read_only=True)
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'content',
                  'summary',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'latestComment',
                  'LocalPublishtime',
                  'author',
                  )
        
        
class RcmdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'content',
                  'summary',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'readStatus',
                  'LocalPublishtime',
                  )
