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