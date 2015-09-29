#coding=utf-8
from django.shortcuts import render
from rest_framework import generics
from .serializers import POISerializer
from rest_framework.response import Response

# Create your views here.
class POIList(generics.ListAPIView):
    """ 评论列表，继承generic view,<br>
        /api/comments/530/?pgsize=10&page=2
        
    """
    #queryset = Comment.objects.all()
    serializer_class = POISerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenizedURLAuthentication,)
    paginate_by = 10
    paginate_by_param = 'pgsize'
    max_paginate_by = 100
    
    def get_queryset(self):
        '''
         loc: 逗号分开如 343,234
        '''
        q = self.kwargs['q']
        loc = self.kwargs['loc'].split(',')
        radius = self.kwargs.get('radius',1000)
        return Response(POI.arounds.search(q=q, loc=loc, radius=radius))
    