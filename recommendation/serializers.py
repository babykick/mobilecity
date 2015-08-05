#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem
from .models import Comment, Tag
from users.serializers import AuthorSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',
                  )
    

class RcmdItemEntrySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'content',
                  'summary',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'hotestComment',
                  'LocalPublishtime',
                  'author',
                  'upCount',
                  'downCount',
                  'tags',
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


