#coding=utf-8
import requests
import lxml.html
import lxml.etree
import pprint


class MeituanAPI(object):
    cookies = {'ci': '267'}
    api_url = 'http://api.union.meituan.com/data/api'
    token = '3f8dd7854089f750b46901bc2a269227556'
    
    
    @classmethod
    def search_detail(self, keyword):
        paras = {
          'w': keyword,
          'mtt':'1.index/floornew.0.0.icwn0xg9'
        }
        
        content = requests.get('http://chs.meituan.com/s/', params=paras, cookies=self.cookies).content
        #print content
        doc = lxml.html.fromstring(content)
        return doc.xpath("//div[contains(concat(' ', @class, ' '), ' deal-tile ')]")
    
    @classmethod 
    def search(self, keyword, city=None, cate=None):
        """ 来自美团联盟api
            http://api.union.meituan.com/data/api?city=%E5%B2%B3%E9%98%B3&category=%E7%BE%8E%E9%A3%9F&limit=10&key=3f8dd7854089f750b46901bc2a269227556&keyword=%E4%B8%89%E6%AF%9B&sort=1
            返回xml
            文档见doc/美团请求API使用说明.docx
        """
        params = {
            'limit': '10',
            'key': self.token,
            'keyword': keyword,
            'sort': '1'
        }
        if city: params.update({'city':city})
        if cate: params.update({'category': cate})
        content = requests.get(self.api_url, params=params).content
        print(content)
        doc = lxml.etree.fromstring(content)
        return doc.xpath('//shop')
        
if __name__ == '__main__':
    print MeituanAPI.search('口味虾', city=u'岳阳')
    