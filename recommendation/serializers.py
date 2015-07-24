#coding=utf-8
from rest_framework import serializers
from .models import RecommendItem


class RcmdItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendItem
        fields = ('title', 'content')
