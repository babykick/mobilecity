# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
# import sys, os
# sys.path.append('F:\\programing\\python\\app\\webprojects\\django\\mobilecity')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lordrecommender.settings")

#from recommendation.models import RecommendItem
# class RecommendItemEntry(DjangoItem):
#     django_model = RecommendItem


class MeituanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    imgurl = scrapy.Field()



