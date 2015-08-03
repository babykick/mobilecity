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
from users.auth import TokenizedURLAuthentication

from recommendation.models import RecommendItem
from recommendation.serializers import RcmdItemEntrySerializer,RcmdDetailSerializer
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class RecommendList(APIView):
    """
    List all recommendations, or create a new recommendation.<br>
    API Parameters<br>
    =============<br>
    n: Item num in a page </BR>
    page: Page index, start from 1  </BR>
    format: json   </BR>
    token: required, as a developer, should be with the url at invoking, example: </BR></BR>
    http://127.0.0.1:8000/api/rcmdlist/?n=5&page=2&format=json&token=d16a8d11c10afeabcdef64be5457b3c669467adb  </BR>
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
        rcmds = RecommendItem.objects.all().order_by('publishTime')
        paginator = Paginator(rcmds, eachnum) # Show 25 contacts per page
        try:
            rs = paginator.page(page)
        except EmptyPage:
            rs = paginator.page(paginator.num_pages)
        serializer = RcmdItemEntrySerializer(rs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = RcmdItemEntrySerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RecommendDetail(APIView):
    """
    Retrieve a recommendation with detailed information,
    or update/delete a recommendation instance.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,  )
    authentication_classes = (TokenizedURLAuthentication,)
    
    
    def get_object(self, pk):
        try:
            return RecommendItem.objects.get(pk=pk)
        except RecommendItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        r = self.get_object(pk)
        serializer = RcmdDetailSerializer(r)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     rcmd = self.get_object(pk)
    #     serializer = RcmdSerializer(rcmd, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 
    # def delete(self, request, pk, format=None):
    #     rcmd = self.get_object(pk)
    #     rcmd.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


