from django.test import TestCase
from .models import RecommendItem
import json
import requests
        
class JsonTestCase(TestCase):
    def setUp(self):
        self.objs = RecommendItem.objects.all()
    
    def test_json_encoding(self):
       
        data = requests.get('http://111.8.186.228:8000/api/rcmdlist/?format=json').content
        jsonobj = json.loads(data)