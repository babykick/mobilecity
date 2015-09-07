#coding=utf-8
import requests
try:
    import ujson as json
except ImportError:
    print "simplejson instead"
    import simplejson as json
import lxml.html    
    
class BaiduMap:
    """ 百度地图API
        
        官方文档：
        POI: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """
    token = "C2bfc69b56baa2abd66ae613966ed3d9"
    url = "http://api.map.baidu.com/place/v2/search"
    
    @classmethod
    def search_POI(self, q):
        """ 搜索poi
            q: 搜索关键字，如公厕，饭店，餐馆，洗浴
        """
        
        params = {'query': q,  
                  'output':'json',
                  'ak': self.token,
                  'scope': 2,
                  'region': u'岳阳'
        }
        ret = requests.get(self.url, params=params).text
        jsonobj = json.loads(ret)
        return jsonobj
    
    @classmethod
    def search_detail(self):
        url = 'http://map.baidu.com/detail?qt=caterphoto&uid=cd9d05dd7e197daf84420eb6&type=list&ugc_ver=1'
        doc = lxml.html.fromstring(requests.get(url).text)
        div = doc.xpath("//div[contains(@class, 'more-comments')]")[0]
        dzdp, meituan, dcms, globalview, qqfood = div.xpath("./span/a/@href")
        print dzdp, meituan, dcms, globalview, qqfood
        print requests.get(meituan, allow_redirects=True).content 
    
    
    @classmethod
    def search_distance(self, q, loc, radius):
        """ 搜索周边
            q: 搜索关键字，如公厕，饭店，餐馆，洗浴
            loc: tuple (lat, lng)
            radius: 半径（米)
            output: json or xml
            ak: token
            scope: 1 为列表， 2为详细信息
               
        """
        url = "http://api.map.baidu.com/place/v2/search"
        params = {'query': q, # 饭店
                  'location': "%s,%s" % loc, #39.915,116.404,
                  'radius':radius,
                  'output':'json',
                  'ak': self.token,
                  'scope': 2
        }
        ret = requests.get(self.url, params=params).text
        return json.loads(ret)
    

if __name__ == '__main__':
    res = BaiduMap.search_distance(q=u'饭店', loc=(39.915,116.404), radius=1000)
    print BaiduMap.search_detail()
    
    
