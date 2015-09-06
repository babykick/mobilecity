from django.test import TestCase
import ujson
import requests

# Create your tests here.
class Test(TestCase):
    def test_poi_search(self):
        data={"token":'d16a8d11c10afef6592264be5457b3c669467adb',
              "q":'cake'}
        r = requests.post('http://127.0.0.1:8000/api/poi/search/', data=data)
        self.assertEqual(ujson.loads(r.text)['result'], 'ok')

