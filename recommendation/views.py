#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from recommendation.models import RecommendItem
from recommendation.serializers import RcmdItemEntrySerializer,RcmdDetailSerializer
from django.http import HttpResponse
 

class RecommendList(APIView):
    """
    List all recommendations, or create a new recommendation.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    #renderer_classes = (JSONRenderer, )
    
    def toUTF8(self, data):
        for record in data:
            record['title'] 
          
    def toHttpResponse(self, data): 
        return HttpResponse(json.dumps(self.toUTF8(data),ensure_ascii="False"), content_type='application/json; charset=utf-8')
    
    def get(self, request, format=None):
        """
           http://127.0.0.1:8000/api/rcmdlist/?format=json
        """
        rcmds = RecommendItem.objects.all()
        serializer = RcmdItemEntrySerializer(rcmds, many=True)
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
    Retrieve, update or delete a recommendation instance.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
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


