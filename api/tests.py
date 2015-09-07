#coding=utf-8
from django.test import TestCase
import ujson
import requests
import pprint
from BaiduMapAPI import BaiduMap

# Create your tests here.
class Test(TestCase):
    def test_poi_search_food(self):
        data={"token":'d16a8d11c10afef6592264be5457b3c669467adb',
              "q":u'三毛',
              'category': u'美食'}
        r = requests.post('http://127.0.0.1:8000/api/poi/search/', data=data)
        content = ujson.loads(r.text)
        self.assertEqual(content['message'], 'ok')
        
    def test_poi_search_book(self):
        data={"token":'d16a8d11c10afef6592264be5457b3c669467adb',
              "q":'乌合之众',
              'category': u'图书'}
        r = requests.post('http://127.0.0.1:8000/api/poi/search/', data=data)
        content = ujson.loads(r.text)
        self.assertEqual(r.status_code, 200)
        
    def test_poi_detail(self):
        BaiduMap.search_detail()



