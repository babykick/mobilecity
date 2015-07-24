from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from recommendation.models import RecommendItem
from recommendation.serializers import RcmdItemSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
        
@csrf_exempt
def rcmd_list(request):
    """
    List all recommendations
    """
    if request.method == 'GET':
        rcmds = RecommendItem.objects.all()
        serializer = RcmdItemSerializer(rcmds, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RcmdItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)        




@csrf_exempt
def rcmd_detail(request, pk):
    """
    Retrieve, update or delete a recommendation item
    """
    try:
        rcmds = RecommendItem.objects.get(pk=pk)
    except RecommendItem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RcmdItemSerializer(snippet)
        return JSONResponse(serializer.data)
