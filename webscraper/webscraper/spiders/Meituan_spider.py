#coding=utf-8
import scrapy
from webscraper.items import MeituanItemEntry

class MeituanSpider(scrapy.Spider):
    name = 'meituan_spider'
    allowed_domains = ["meituan.com"]
    start_urls = [
       "http://yy.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.icwt533g"
    ]
    
    def parse(self, response):
        for sel in response.xpath("//div[contains(concat(' ', @class, ' '), ' poi-tile-nodeal ')]"):
            if sel:
                item = MeituanItemEntry()
                title = sel.xpath(".//div[@class='basic cf']/a/text()").extract()[0]
                item['summary'] = item['title']
                item['content'] = item['title']
                item['picOne'] = sel.xpath(".//img[@class='J-webp']/@src").extract()[0]
                item['picTwo'] = item['picOne']
                item['picThr'] = item['picOne'] 
                yield item
         