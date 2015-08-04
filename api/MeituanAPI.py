#coding=utf-8
import requests
import lxml.html
s = requests.Session()

class MeituanAPI(object):
    cookies = {'ci': '267'}
    
    @classmethod
    def search(self, keyword):
        paras = {
          'w': keyword,
          'mtt':'1.index/floornew.0.0.icwn0xg9'
        }
        
        content = requests.get('http://chs.meituan.com/s/', params=paras, cookies=self.cookies).content
        #print content
        doc = lxml.html.fromstring(content)
        return doc.xpath("//div[contains(concat(' ', @class, ' '), ' deal-tile ')]")
       
if __name__ == '__main__':
    print MeituanAPI.search('口味虾')
    