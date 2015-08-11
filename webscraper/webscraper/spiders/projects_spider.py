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
from bs4 import BeautifulSoup
import lxml.etree

# os.environ["http_proxy"] = "http://127.0.0.1:8087"
# os.environ["https_proxy"] = "https://127.0.0.1:8087"

cloned_cookies = dict(sign='CFj72NzSIr', csrf_cname='76e61f7e9e1b966f96b753ed5bb87dbe', session_name='20991504217384047261787419691597258114', spksrc_ut='61f06092747ae7f5b477998e7b931a72', session_flag='2', duoshuo_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaG9ydF9uYW1lIjoiY3JlYXRpdmUiLCJ1c2VyX2tleSI6IjI4NDg1MCIsIm5hbWUiOiIxMzkwNzMwOTIwNiJ9.xlMwz-ZyzdTz2qvHfAGSUCMRUQdGKY5M3TraZNlAL00', sso_token='e694513609d7392922144c753152f02e22175834')
  

class ProjectSpider(scrapy.Spider):
    name = 'projectspider'
    allowed_domains = ['bigcloudsys.cn']
    login_page = 'http://zzkf.bigcloudsys.cn:8088/user/login' # login page url
    login_url = 'http://zzkf.bigcloudsys.cn:8088/user/loginDo' # url for post
    home_page = 'http://zzkf.bigcloudsys.cn:8088'
    #start_urls = ['http://zzkf.bigcloudsys.cn:8088/welcome/ajax_get/?&csrf_tname=2d85a35e4b576e09f0eb9411c2920ecf']
    ajax_prefix = 'http://zzkf.bigcloudsys.cn:8088/welcome/ajax_get/?'
    rank_url_prefix = 'http://zzkf.bigcloudsys.cn:8088/project/ajax_lists'
    
    
    def start_requests(self):
        """Generate a login request."""
        payload = {
            'ajax':	'2',
            'csrf_tname':	'76e61f7e9e1b966f96b753ed5bb87dbe',
            'loginName':	'13907309206',
            'loginPwd':	'Hacker1218',
        }
        self.prefix = self.rank_url_prefix
        self.pgIndexName = 'start_info'
 
        return [FormRequest(url=self.login_url,
                            formdata=payload,
                            cookies=cloned_cookies,
                            callback=self.check_login_response)]

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        msg = json.loads(response.body_as_unicode())['msg']
        if u"登录成功" in msg:
            self.log("Successfully logged in. Let's start crawling!")
            return Request(url=self.home_page, callback=self.parse_ranked_links)
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
    
    
    def parse_all_projects_links(self, response):
        # Now the crawling can begin..
        numeachpage = 12
        total = 400
        for start in range(1, total, numeachpage):
            url = self.prefix + urllib.urlencode({'start': self.pgIndexName,
                                     'csrf_tname':'2d85a35e4b576e09f0eb9411c2920ecf'
                                    })
            yield Request(url=url, callback=self.parse_page)
            
    
    def parse_ranked_links(self, response):
         # Now the crawling can begin..
        pageTotal = 40
        for pg in range(1, pageTotal, 1):
            url = self.rank_url_prefix + '/0/0/3/%s?' % pg + \
                   urllib.urlencode({'start_info': pg,
                                     'csrf_tname':'2d85a35e4b576e09f0eb9411c2920ecf'
                                   })
            req = Request(url=url, callback=self.parse_page)
            req.meta['page'] = pg
            yield req
     
        
    def parse_page(self, response):
        """
           Parse each page
        """
        html = json.loads(response.body_as_unicode())['msg']
        if html.strip():
            sel = Selector(text=html, type="html")
            index = 1
            for elem in sel.xpath("//ul[contains(@class,'project-one')]"):
                try:
                    item = ProjectItem()
                    item["link"] = elem.xpath(".//li[@class='project-thumbnail']/a/@href").extract_first(default='')
                    item["title"] = elem.xpath(".//li[@class='project-titile']/a/text()").extract_first(default='')
                    item["summary"]  = BeautifulSoup(elem.xpath(".//li[@class='project-descrip']/a/@title").extract_first(default='')).text
                    item["pubtime"] = elem.xpath(".//li[@class='project-list-stats']/a[@class='p-time']/text()").extract_first(default='')
                    item["rank"] = str((response.meta['page'] -1) * 8 + index)
                    # item["department"]
                    #print elem.xpath(".//li[contains(@class, 'project-function')]/p").extract()#.re(r'span(.*?)span')
                    #print elem.xpath(".//li[contains(@class, 'project-function')]/p/comment()").extract()
                    yield item
                    index += 1
                except Exception, e:
                    print e
        
   