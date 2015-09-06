import json
import requests
import chardet
import pprint


def test_list_api():
   url = 'http://111.8.186.228:8000/api/rcmdlist/?n=100&page=1&format=json&token=d16a8d11c10afef6592264be5457b3c669467adb'
   data = requests.get(url).json()
   print data
   
def test_redis():
    import redis
    r = redis.Redis(host='127.0.0.1', db=0)
    r.sadd("testset", "apple")
    
if __name__ == "__main__":
    # test_redis()
   

 