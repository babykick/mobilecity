from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from recommendation.models import RecommendItem
from recommendation.serializers import RcmdItemSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser



class RecommendList(APIView):
    """
    List all recommendation, or create a new recommend.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    
    def get(self, request, format=None):
        """
           http://127.0.0.1:8000/api/rcmdlist/?format=json
        """
        rcmds = RecommendItem.objects.all()
        serializer = RcmdItemSerializer(rcmds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RcmdItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RecommendDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return RecommendItem.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RcmdSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rcmd = self.get_object(pk)
        serializer = RcmdSerializer(rcmd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rcmd = self.get_object(pk)
        rcmd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 
# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#         
#         
# @csrf_exempt
# def rcmd_list(request):
#     """
#     List all recommendations
#     """
#     if request.method == 'GET':
#         rcmds = RecommendItem.objects.all()
#         serializer = RcmdItemSerializer(rcmds, many=True)
#         return JSONResponse(serializer.data)
# 
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = RcmdItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)        
# 
# 
# 
# 
# @csrf_exempt
# def rcmd_detail(request, pk):
#     """
#     Retrieve, update or delete a recommendation item
#     """
#     try:
#         rcmds = RecommendItem.objects.get(pk=pk)
#     except RecommendItem.DoesNotExist:
#         return HttpResponse(status=404)
# 
#     if request.method == 'GET':
#         serializer = RcmdItemSerializer(snippet)
#         return JSONResponse(serializer.data)
