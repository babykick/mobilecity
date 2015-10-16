#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics
from users.auth import TokenizedURLAuthentication
from recommendation.models import RecommendItem, Comment
from recommendation.serializers import RcmdItemEntrySerializer, RcmdDetailSerializer, CommentSerializer
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from api.baiduAPI import BaiduMap
from api.doubanAPI import DoubanAPI
from .tasks import add

# First, define the Manager subclass.

class RecommendList(APIView):
    """
    List all recommendations, or create a new recommendation.<br>
    Example:  http://127.0.0.1:8000/api/rcmdlist/?n=5&page=2&format=json&token=d16a8d11c10afeabcdef64be5457b3c669467adb  </BR></BR>
    API Parameters explain<br>
    =======================<br>
    n: Item num in a page </BR>
    page: Page index, start from 1  </BR>
    format: json   </BR>
    token: required, as a developer, should be with the url at invoking, example: </BR></BR>
   
    Return json list </br>
    ====================== </br>
     [{
        "id": 538,     # id </br>
        "title": "牛太郎时尚烧烤火锅",   # 标题   </br>
        "content": "牛太郎时尚烧烤火锅",  # 内容  </br>
        "summary": "牛太郎时尚烧烤火锅",  # 摘要  </br>
        "picOneURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片一</br>
        "picTwoURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片二</br>
        "picThrURL": "http://p1.meituan.net/350.214/deal/__18252036__7392151.jpg", # 图片三 </br>
        "hotestComment": null,   # 最火评论 </br>
        "localPublishTime": "2015-08-05T11:28:54.097+08:00", # 当地发布时间  </br>
        "author": {    #作者信息</br>
            "id": 1,   </br>
            "nickname": "推主X",    </br>
            "avatar": "http://img3.douban.com/icon/u3823403-2.jpg", </br>
            "level": 100 </br>
        },
        "upCount": 78,  # 赞数</br>
        "downCount": 3,  # 贬数</br>
        "tags": [],   # 标签</br>
        "commentCount": 0, # 评论数 </br>
        "latestComments": [] # 最近5条评论 </br>
      },...]
    """
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    authentication_classes = (TokenizedURLAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    #renderer_classes = (JSONRenderer, )
    

    def get(self, request, format=None):
        """
           doc:  http://127.0.0.1:8000/api/rcmdlist/?n=5&page=2&token=d16a8d11c10afef6592264be5457b3c669467adb
           json: http://127.0.0.1:8000/api/rcmdlist/?n=5&page=2&format=json&token=d16a8d11c10afef6592264be5457b3c669467adb
           TokenizedURLAuthentication gives out (request.auth, request.user)
        """
        page = request.GET.get('page', 1)
        eachnum = request.GET.get('n', 10)
        category = request.GET.get('category', None)
        if category is not None:
            rcmds = RecommendItem.objects.filter(category=category)
        else:
            rcmds = RecommendItem.objects.all()
        rcmds = rcmds.order_by('-publishTime')
        paginator = Paginator(rcmds, eachnum) # Show 25 contacts per page
        try:
            rs = paginator.page(page)
        except EmptyPage:
            rs = paginator.page(paginator.num_pages)
        serializer = RcmdItemEntrySerializer(rs, many=True)
        return Response(serializer.data)

   

class RecommendDetail(APIView):
    """
    Retrieve a recommendation with detailed information,
    or update/delete a recommendation instance.<br>
    example:<br>
    http://111.8.186.228:8000/api/rcmdlist/530/?token=d16a8d11c10afef6592264be5457b3c669467adb
    
    """
    permission_classes = (IsAuthenticatedOrReadOnly,  )
    authentication_classes = (TokenizedURLAuthentication,)
    
    
    def get_object(self, pk):
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
    
    
    def post(self, request, format=None):
        """ 新建RecommendItem
            成功则返回对象的json，否则返回错误信息
        """
        serializer = RcmdDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



class POIDetail(APIView):
    """ 查询POI
        q: 关键字
    """
    permission_classes = (IsAuthenticatedOrReadOnly,  )
    authentication_classes = (TokenizedURLAuthentication,)
    
    def post(self, request, format='json'):
        keyword = request.POST.get('q')
        cate = request.POST.get('category')
        if cate in (u'美食', ):
            ret = BaiduMap.search_POI(keyword)
        elif cate in (u'图书', ):
            ret = DoubanAPI.querybook(q=keyword)
        elif cate in (u'电影', ):
            ret = DoubanAPI.querymovie(q=keyword)
        return Response(ret)
        

class CommentList(generics.ListAPIView):
    """ 评论列表，继承generic view,<br>
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
    
    
    