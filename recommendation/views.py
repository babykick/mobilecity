#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from users.auth import TokenizedURLAuthentication
from recommendation.models import RecommendItem, Comment
from recommendation.serializers import RcmdItemEntrySerializer, RcmdDetailSerializer, CommentSerializer
from api.baiduAPI import BaiduMap
from api.doubanAPI import DoubanAPI
from .tasks import add
from business.serializers import POISerializer
from business.models import POI





class RecommendList(generics.ListAPIView):
    """
    ### 查询所有周边推荐
    * http://localhost:8000/api/rcmdlist/?loc=113.5959367,28.69592534&q=%E7%BE%8E%E9%A3%9F&radius=1000&token=d16a8d11c10afef6592264be5457b3c669467adb
    * loc: 经纬度
    * q: 查询关键字
    * radius: 半径
   
    ### API Parameters explain
    =======================
    * n: Item num in a page 
    * page: Page index, start from 1  
    * format: json   
    * token: required, as a developer, should be with the url at invoking, example: 
   
    #### Return json list 
    ====================== 
     [{
        "id": 538,     # id 
        "title": "牛太郎时尚烧烤火锅",   # 标题   
        "content": "牛太郎时尚烧烤火锅",  # 内容  
        "summary": "牛太郎时尚烧烤火锅",  # 摘要  
        "picOneURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片一
        "picTwoURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片二
        "picThrURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片三 
        "hotestComment": null,   # 最火评论 
        "localPublishTime": "2015-08-05T11:28:54.097+08:00", # 当地发布时间  
        "author": {    #作者信息
            "id": 1,   
            "nickname": "推主X",    
            "avatar": "http://img3.douban.com/icon/u3823403-2.jpg", 
            "level": 100 
        },
        "upCount": 78,  # 赞数
        "downCount": 3,  # 贬数
        "tags": [],   # 标签
        "commentCount": 0, # 评论数 
        "latestComments": [] # 最近5条评论 
      },...]
    """
    serializer_class = RcmdItemEntrySerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    authentication_classes = (TokenizedURLAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    #renderer_classes = (JSONRenderer, )
    paginate_by_param = 'n'
    paginate_by = 10
    max_paginate_by = 100
    #parser_classes = (FileUploadParser, )
    
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        loc = map(float, self.request.GET.get('loc').split(','))
        radius = self.request.GET.get('radius', 1000)
        if q and loc and radius:
             return RecommendItem.around.search(q, loc, radius)
    
    
    def by_category(self):
        pass
        # 
        # if category is not None:
        #     rcmd_set = RecommendItem.objects.filter(category=category)
        # else:
        #     rcmd_set = RecommendItem.objects.all()
        # return rcmd_set
     

    def post(self, request, format='json'):
        """ 新建RecommendItem
            成功则返回对象的json，否则返回错误信息
        """
        serializer = RcmdDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     
    # def put(self, request, filename, format=None):
    #     file_obj = request.data['file']
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)


class RecommendDetail(generics.GenericAPIView):
    """
    ### Retrieve a recommendation with detailed information, or update/delete a recommendation instance.
   
    example:
    http://111.8.186.228:8000/api/rcmdlist/530/?token=d16a8d11c10afef6592264be5457b3c669467adb
    
    """
    serializer_class = RcmdDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,  )
    authentication_classes = (TokenizedURLAuthentication,)
    
    
    def get_object(self, pk):
        """ 从url获取需要详细的object
        """
        print "in"
        try:
            return RecommendItem.objects.get(pk=pk)
        except RecommendItem.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        """ 获取RecommendItem
            pk: 从url传递过来的id
        """
        r = self.get_object(pk)
        serializer = RcmdDetailSerializer(r)
        return Response(serializer.data)
    
     
    def put(self, request, pk, format=None):
        """ 更新RecommendItem
            pk: 从url传递过来的id
            成功则返回对象的json，否则返回错误信息
        """
        rcmd = self.get_object(pk)
        serializer = RcmdDetailSerializer(rcmd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        """ 删除RecommendItem
            返回状态信息
        """
        rcmd = self.get_object(pk)
        rcmd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class POIDetail(generics.GenericAPIView):
    """ 查询POI
        q: 关键字
    """
    serializer_class = POISerializer
    permission_classes = (IsAuthenticatedOrReadOnly,  )
    authentication_classes = (TokenizedURLAuthentication,)
    
    
    def get_object(self, pk):
        """ 从url获取需要详细的object
        """
        try:
            return POI.objects.get(pk=pk)
        except POI.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):
        raise NotImplemented
        

class CommentList(generics.ListAPIView):
    """ 评论列表，继承generic view,
        /api/comments/530/?pgsize=10&page=2
        
    """
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenizedURLAuthentication,)
    paginate_by = 10
    paginate_by_param = 'pgsize'
    max_paginate_by = 100
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(object_id=pk)
    
    def post(self, request, pk, format=None):
        """ Comment post
            成功则返回对象的json，否则返回错误信息
        """
        print request.data
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    