# Show a map
"""
	 <style>
	   .iphone iframe{width: 950px;height: 564px;border: none;overflow: hidden;margin: 10px 0 0 32px;}
	 </style>
	 <div class="iphone">
	   <iframe id="iphone_iframe" src="http://m.amap.com/navi/?dest=116.470098,39.992838&amp;destName=阜通西&amp;hideRouteIcon=1&amp;key=d3f5d8b3b05231fa6a11375492310e3a" frameborder="0"></iframe>
	 </div>

"""     
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

 
def toHttpResponse(self, data): 
        return HttpResponse(json.dumps(self.toUTF8(data),ensure_ascii="False"), content_type='application/json; charset=utf-8')
            
        
@csrf_exempt
def rcmd_list(request):
    """
    List all recommendations
    """
    if request.method == 'GET':
        rcmds = RecommendItem.objects.all()
        serializer = RcmdItemEntrySerializer(rcmds, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RcmdItemEntrySerializer(data=data)
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
        serializer = RcmdItemEntrySerializer(snippet)
        return JSONResponse(serializer.data)
