#coding=utf-8
import requests
try:
    import ujson as json
except ImportError:
    print "ujson not found, use simplejson instead"
    import simplejson as json
import lxml.html    
 
MAIN_TOKEN = "C2bfc69b56baa2abd66ae613966ed3d9"


class BaiduMap:
    """ 百度地图API
        
        官方文档：
        POI: http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-placeapi
    """
    token = MAIN_TOKEN
    url = "http://api.map.baidu.com/place/v2/search"
    
    
    @classmethod
    def search_POI(self, q, city):
        """ 搜索poi
            q: 搜索关键字，如公厕，饭店，餐馆，洗浴
        """
        
        params = {'query': q,  
                  'output':'json',
                  'ak': self.token,
                  'scope': 2,
                  'region': city
        }
        ret = requests.get(self.url, params=params).text
        jsonobj = json.loads(ret)
        return jsonobj
    
    
    @classmethod
    def search_detail(self):
        s = requests.Session()
        url = 'http://map.baidu.com/detail?qt=caterphoto&uid=cd9d05dd7e197daf84420eb6&type=list&ugc_ver=1'
        r = requests.get(url)
        cookies = r.cookies
        doc = lxml.html.fromstring(r.text)
        div = doc.xpath("//div[contains(@class, 'more-comments')]")[0]
        #dzdp, meituan, dcms, globalview, qqfood
        links = div.xpath("./span/a/@href")
        dzdp, meituan, dcms, globalview, qqfood = links
        print meituan
        print s.get(meituan, cookies=cookies).content 
        
    
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
                  'location': "%s,%s" % tuple(loc), #39.915,116.404,
                  'radius':radius,
                  'output':'json',
                  'ak': self.token,
                  'scope': 2
        }
        ret = requests.get(self.url, params=params).text
        return json.loads(ret)


class BaiduAPIStore:
    """ 百度APIStore, api集合
        doc: http://apistore.baidu.com/
    """
    token = MAIN_TOKEN
    
    def search_nuomi(self):
        """ 糯米商户信息及团购搜索
            文档地址:http://apistore.baidu.com/apiworks/servicedetail/508.html
        """
        pass
    
    def search_movie(self):
        """ 搜索影讯
            文档地址：http://apistore.baidu.com/apiworks/servicedetail/189.html
        """
        pass
    
    
    def search_near(self):
        """ 搜索周边
            文档地址： http://apistore.baidu.com/apiworks/servicedetail/469.html
        """
        pass
    
    
    def search_qunaer(self):
        """ 去哪儿景点门票查询
            文档地址： http://apistore.baidu.com/apiworks/servicedetail/140.html
        """
        pass
    
    
    
    
if __name__ == '__main__':
    import pprint
    pprint.pprint(BaiduMap.search_distance(q=u'饭店', loc=(39.915,116.404), radius=1000))
    #pprint.pprint(BaiduMap.search_POI(u'山上铺里', city=u'岳阳'))
    
    
