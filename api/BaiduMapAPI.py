#coding=utf-8
import requests
try:
    import ujson as json
except ImportError:
    print "simplejson instead"
    import simplejson as json
    
class BaiduMap:
    """ 百度地图API
        
        官方文档：
        POI: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """
    token = "C2bfc69b56baa2abd66ae613966ed3d9"
    
    @classmethod
    def search(self, q, loc, radius):
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
        ret = requests.get(url, params=params).text
        return json.loads(ret)
    

if __name__ == '__main__':
    res = BaiduMap().search(q=u'饭店', loc=(39.915,116.404), radius=1000)
    print res
    
    
