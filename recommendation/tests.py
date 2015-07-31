from django.test import TestCase

# Create your tests here.
 
from .models import RecommendItem

class JsonTestCase(TestCase):
    def setUp(self):
        self.objs = RecommendItem.objects.all()
    
    def test_json_encoding(self):
        import json
        import requests
        data = requests.get('http://111.8.186.228:8000/api/rcmdlist/?format=json').content
        jsonobj = json.loads(data)