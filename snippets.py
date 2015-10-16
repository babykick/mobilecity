# Show a map
"""
	 <style>
	   .iphone iframe{width: 950px;height: 564px;border: none;overflow: hidden;margin: 10px 0 0 32px;}
	 </style>
	 <div class="iphone">
	   <iframe id="iphone_iframe" src="http://m.amap.com/navi/?dest=116.470098,39.992838&amp;destName=阜通西&amp;hideRouteIcon=1&amp;key=d3f5d8b3b05231fa6a11375492310e3a" frameborder="0"></iframe>
	 </div>

"""

# 按content_type和object_id搜索
>>> b = Bookmark.objects.get(url='https://www.djangoproject.com/')
>>> bookmark_type = ContentType.objects.get_for_model(b)
>>> TaggedItem.objects.filter(content_type__pk=bookmark_type.id,
...                           object_id=b.id)


  def get_deprecated(self, request, format=None):
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
    
     
def import_data():
    import os
    import django
    import json
    
    # Setup django standalone environment
    os.environ['DJANGO_SETTINGS_MODULE'] = 'lordrecommender.settings'
    django.setup()
    from recommendation.models import RecommendItem
    
    jsondata = json.load(open('webscraper/data/meituan_food2.json'))
    for a in jsondata:
        item = RecommendItem()
        item.picOne = a.get('imgurl')[0]
        item.picTwo = item.picOne 
        item.picThr = item.picOne 
        item.title = a.get('title')[0]
        item.summary = item.title
        item.content = item.title
        item.save()


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
