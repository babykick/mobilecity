import json
import requests
import chardet
import pprint
data = requests.get('http://111.8.186.228:8000/api/rcmdlist/?format=json').content
print chardet.detect(data)
pprint.pprint([data])
jsonobj = json.loads(data)
 