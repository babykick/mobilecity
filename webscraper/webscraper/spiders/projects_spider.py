#coding=utf-8
import scrapy
from scrapy.spiders.init import InitSpider
from scrapy.http import Response, FormRequest, Request
from scrapy import Selector
from scrapy.exceptions import CloseSpider
from webscraper.items import ProjectItem
import json
import urllib
import os

# os.environ["http_proxy"] = "http://127.0.0.1:8087"
# os.environ["https_proxy"] = "https://127.0.0.1:8087"

cloned_cookies = dict(sign='CFj72NzSIr', csrf_cname='76e61f7e9e1b966f96b753ed5bb87dbe', session_name='20991504217384047261787419691597258114', spksrc_ut='61f06092747ae7f5b477998e7b931a72', session_flag='2', duoshuo_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaG9ydF9uYW1lIjoiY3JlYXRpdmUiLCJ1c2VyX2tleSI6IjI4NDg1MCIsIm5hbWUiOiIxMzkwNzMwOTIwNiJ9.xlMwz-ZyzdTz2qvHfAGSUCMRUQdGKY5M3TraZNlAL00', sso_token='e694513609d7392922144c753152f02e22175834')
  

class ProjectSpider(InitSpider):
    name = 'projectspider'
    allowed_domains = ['bigcloudsys.cn']
    login_page = 'http://zzkf.bigcloudsys.cn:8088/user/login' # login page url
    login_url = 'http://zzkf.bigcloudsys.cn:8088/user/loginDo' # url for post
    start_urls = ['http://zzkf.bigcloudsys.cn:8088/welcome/ajax_get/?&csrf_tname=2d85a35e4b576e09f0eb9411c2920ecf']
    
    
    # rules = (
    #     Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
    #          callback='parse_item', follow=True),
    # )

    def init_request(self):
        #request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        """This function is called before crawling starts."""
        return Request(url=self.login_page,
                       cookies=cloned_cookies,
                       callback=self.login)

    def login(self, response):
        """Generate a login request."""
        payload = {
            'ajax':	'2',
            'csrf_tname':	'76e61f7e9e1b966f96b753ed5bb87dbe',
            'loginName':	'13907309206',
            'loginPwd':	'Hacker1218',
        }
        return FormRequest.from_response(response,
                                         formdata=payload,
                                         callback=self.check_login_response,
                                         url=self.login_url
                                         )


    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        msg = json.loads(response.body_as_unicode())['msg']
        if u"登录成功" in msg:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            return self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.


    def parse(self, response):
        """
          Construct each page url to distribute 
        """
        #request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        self.log("Start parsing!!!!!!!!!")
        numeachpage = 12
        page = 0
        items = []
        while True:
            print 'Scanning page', page + 1
            url = 'http://zzkf.bigcloudsys.cn:8088/welcome/ajax_get/?'
            url += urllib.urlencode({'start': numeachpage * page + 1,
                                     'csrf_tname':'2d85a35e4b576e09f0eb9411c2920ecf'
                                    })
            yield Request(url, callback=self.parse_page)
            page += 1
            if page > 400 / 12 :
                break
        
    def parse_page(self, response):
        """
           Parse each page
        """
        html = json.loads(response.body_as_unicode())['msg']
        #print 'html: ', html
        if html.strip():
            sel = Selector(text=html, type="html")
            for elem in sel.xpath("//ul[contains(@class,'project-one')]"):
                try:
                    item = ProjectItem()
                    item["link"] = elem.xpath(".//li[1]/a/@href").extract()[0]#.replace(r'\"', "").replace("\\", '').strip()
                    item["title"] = elem.xpath(".//li[2]/a/text()").extract()[0]
                    item["summary"] = elem.xpath(".//li[3]/a//text()").extract()[0]
                    item["pubtime"] = elem.xpath(".//li[5]/a[2]/text()").extract()[0]
                    yield item
                except Exception, e:
                    print e
        
        
                    
         
   