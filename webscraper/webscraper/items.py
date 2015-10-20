# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
import djangostandalonesetup
from recommendation.models import RecommendItem

 
class DianpingItem(scrapy.Item):
    """
       board -> {'board_title':xx, 'board_url':xx, 'board_intro':xx}    
    """
    board = scrapy.Field() 
    title = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
    coord = scrapy.Field() # (lng, lat)
    region = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    specials_url = scrapy.Field()
    recommends = scrapy.Field()
    reason = scrapy.Field()
    
 
class RecommendItemEntry(DjangoItem):
    django_model = RecommendItem


class ProjectItem(scrapy.Item):
     link = scrapy.Field()
     title = scrapy.Field() 
     summary = scrapy.Field()
     pubtime = scrapy.Field()
     department = scrapy.Field()
     rank = scrapy.Field()

class DocItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
     