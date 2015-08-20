#coding=utf-8
import requests

def build_cookie():
    res = map(str.split , open("dumpedcookie.txt").read().split("\n"))
    cookies = {line[0]:line[2] for line in res if line[1]=="Sent"}
    return cookies
     

class DzdpAPI:
    """
      官方文档： 
    """
    appKey = "5589931241";  
    secret = "db16adf193f2448ba0ec0260e0c968f3"; 

class DzdpHTMLAPI:
    """ 大众点评api
    
    """
    
    def search(self, q, cityid, pg):
        """
           q: 关键字
           cityid: 城市id
           pg: 页码，从1开始
        """
        url = u"http://www.dianping.com/search/keyword/%s/0_%s/%s" % (cityid, q, pg)
        print url
        return requests.get(url,cookies=build_cookie()).content
    
if __name__ == '__main__':
    print DzdpHTMLAPI().search(u'龙虾', 196, 1)
    