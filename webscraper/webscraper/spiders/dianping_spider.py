# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class DianpingSpiderSpider(scrapy.Spider):
    name = "dianping_spider"
    allowed_domains = ["dianping.com"]
    # start_urls = (
    #     'http://www.dianping.com/mylist/yueyang',
    # )
    
    
    
    def start_requests(self, city="yueyang"):
        url = 'http://www.dianping.com/mylist/%s' % city
        r = Request(url=url,
                    # cookies={'JSESSIONID': '02752BCB5C11756EBEB6EB63BF95233E',
                    #                   'PHOENIX_ID': '0a03052a-1507fbe0a52-124ab',
                    #                  # '_hc.v', "\"9dc4f8fe-83aa-4ab2-a7e7-10d225cf471e.1437123244\"",
                    #                   },
                    callback=self.parse)
        #r.meta['proxy'] = "http://127.0.0.1:8087"
        yield r
    
    def parse(self, response):
        print response.body

    def parse_detail(self, response):
        coord = response.xpath("//script").re("lng:(.*?),lat:(.*?)")