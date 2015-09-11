#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem
from .models import Comment, Tag
from users.serializers import AuthorSerializer
from business.models import Location
from business.serializers import LocationSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',
                  )
    
        
class CommentSerializer(serializers.ModelSerializer):
    author= AuthorSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id',
                  'content',
                  'author',
                  'localPublishTime',
                 )
        

        
class RcmdItemEntrySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    latestComments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'summary',
                  'category',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'hotestComment',
                  'localPublishTime',
                  'pubElapse',
                  'author',
                  'upCount',
                  'downCount',
                  'tags',
                  'commentCount',
                  'latestComments',
                  )
        
        
class RcmdDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
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
                  'localPublishTime',
                  'author',
                  'location',
                  'upCount',
                  'downCount',
                  'tags',
                  #'commentCount',
                  #'latestComments',
                  )


