#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem


class RcmdItemEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'content',
                  'summary',
                  'comment',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL'
                  )
        
        
class RcmdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendItem
        fields = ('id',
                  'title',
                  'content',
                  'summary',
                  'comment',
                  'picOneURL',
                  'picTwoURL',
                  'picThrURL',
                  'readStatus',
                  )
