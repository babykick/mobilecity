import json
import requests
import chardet
import pprint


url = 'http://111.8.186.228:8000/api/rcmdlist/?n=100&page=1&format=json&token=d16a8d11c10afef6592264be5457b3c669467adb'
data = requests.get(url).json()
print data


 