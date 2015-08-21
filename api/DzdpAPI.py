#coding=utf-8
import requests
import lxml.html
from  items import DzdpItem


def build_cookie():
    res = map(str.split , open("dumpedcookie.txt").read().split("\n"))
    cookies = {line[0]:line[2] for line in res  }
    return cookies
     

class DzdpAPI:
    """
      官方文档： 
    """
    appKey = "5589931241";  
    secret = "db16adf193f2448ba0ec0260e0c968f3"; 
    proxies = {'http': 'http://127.0.0.1:8087',
               'https': 'http://127.0.0.1:8087'
               }
    
class DzdpHTMLAPI:
    """ 大众点评api
    
    """
    proxies = {'http': 'http://127.0.0.1:8087',
               'https': 'http://127.0.0.1:8087'
               }
    
    def search(self, q, cityid, pg):
        """
           q: 关键字
           cityid: 城市id
           pg: 页码，从1开始
        """
        url = u"http://www.dianping.com/search/keyword/%s/0_%s/%s" % (cityid, q, pg)
        content = requests.get(url,cookies=build_cookie() ).content
        print content
        doc = lxml.html.fromstring(content)
        for li in doc.xpath("//div[@id='shop-all-list']/ul/li"):
            item = DzdpItem()
            item['pic_thumb'] = li.xpath("./div[@class='pic']/a/img")[0].attrib.get('data-src')
            print item
    
if __name__ == '__main__':
    print DzdpHTMLAPI().search(u'龙虾', 196, 1)
    