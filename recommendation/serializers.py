#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem
from .models import Comment, Tag
from users.serializers import AuthorSerializer
from business.models import Location, POI
from business.serializers import LocationSerializer, POISerializer

 
class CommentedObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        """
        Serialize bookmark instances using a bookmark serializer,
        and note instances using a note serializer.
        """
        
        if isinstance(value, RecommendItem):
            serializer = RcmdDetailSerializer(value)
        elif isinstance(value, POI):
            serializer = POISerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

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
                  'object_id',
                 )
        

        
class RcmdItemEntrySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    #latestComments = CommentSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)
    
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'uid',
                  'title',
                  'summary',
                  'category',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'isLarge',
                  'localPublishTime',
                  'pubElapse',
                  'author',
                  'upCount',
                  'location',
                  'downCount',
                  'tags',
                  'commentCount',
                  'coordinate',
                  #'latestComments',
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
                  #'tags',
                  'commentCount',
                  )


