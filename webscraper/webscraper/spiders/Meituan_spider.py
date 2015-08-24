#coding=utf-8
import scrapy
from webscraper.items import MeituanItemEntry
from .. import djangostandalonesetup
from business.models import GeoEntity
from scrapy.linkextractors import LinkExtractor

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
                item['title'] = sel.xpath(".//div[@class='basic cf']/a/text()").extract()[0]
                item['summary'] = item['title']
                item['content'] = item['title']
                item['picOne'] = sel.xpath(".//img[@class='J-webp']/@src").extract()[0]
                item['picTwo'] = item['picOne']
                item['picThr'] = item['picOne']
                taglist = sel.xpath(".//div[@class='tag-list']/a/text()").extract()
                # geo = GeoEntity(description=taglist[1])
                # geo.save()
                # item['geo'] = geo
                item['category'] = taglist[0]
                yield item
         