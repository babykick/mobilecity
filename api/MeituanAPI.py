#coding=utf-8
import requests
import lxml.html
 
class MeituanAPI(object):
    cookies = {'ci': '267'}
    api_url = 'http://api.union.meituan.com/data/api'
    token = '3f8dd7854089f750b46901bc2a269227556'
    
    
    @classmethod
    def search_html(self, keyword):
        paras = {
          'w': keyword,
          'mtt':'1.index/floornew.0.0.icwn0xg9'
        }
        
        content = requests.get('http://chs.meituan.com/s/', params=paras, cookies=self.cookies).content
        #print content
        doc = lxml.html.fromstring(content)
        return doc.xpath("//div[contains(concat(' ', @class, ' '), ' deal-tile ')]")
    
    @classmethod 
    def search(self, keyword):
        """ 来自美团联盟api
            http://api.union.meituan.com/data/api?city=%E5%B2%B3%E9%98%B3&category=%E7%BE%8E%E9%A3%9F&limit=10&key=3f8dd7854089f750b46901bc2a269227556&keyword=%E4%B8%89%E6%AF%9B&sort=1
        """
        params = {
            'city': '岳阳',
            'category': '美食',
            'limit': '10',
            'key': self.token,
            'keyword': keyword,
            'sort': '1'
        }
        print requests.get(self.api_url, params=params).text
        
if __name__ == '__main__':
    print MeituanAPI.search('口味虾')
    