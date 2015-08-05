#coding=utf-8
from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',   
                  'nickname',
                  'avatar',
                  'level',
                  )
        
  