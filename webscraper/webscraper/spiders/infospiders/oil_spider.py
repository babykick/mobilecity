# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from webscraper.infoitems import OilItem


class OilSpiderSpider(scrapy.Spider):
    name = "oil_spider"
     
    
    def __init__(self, region=None, *arg, **kwargs):
        self.region = region
        super(OilSpiderSpider, self).__init__(*arg, **kwargs)
    
    
    def start_requests(self):
        if self.region is not None:
           yield Request("http://youjia.15tianqi.cn/" + self.region + "/", callback=self.parse_oil_price)
        else:
           url = "http://youjia.15tianqi.cn/"
           yield Request(url=url, callback=self.parse)
        
        
    def parse(self, response):
        for link in response.css('.city64').xpath('a/@href').extract():
           yield Request("http://youjia.15tianqi.cn" + link, callback=self.parse_oil_price)
        
    def parse_oil_price(self, response):
        oil_price = response.css('.line_box').css('.content').xpath('p/text()').extract_first()
        date = oil_price.split(',')[0]
        oil_price = oil_price.lstrip(date + ',')
        item = OilItem(price=oil_price, date=date)
        yield item