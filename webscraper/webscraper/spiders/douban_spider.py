#coding=utf-8
import scrapy
from webscraper.items import ItemEntry
import ujson
from scrapy.http import Request
import random
import pprint

class DoubanSpider(scrapy.Spider): 
    name = 'douban_spider'
    book_pattern = "https://api.douban.com/v2/book/series/%s/books"
    
    def start_requests(self):
        for i in random.sample(range(1, 50, 1), 5):
            cate_url = self.book_pattern % i
            yield Request(url=cate_url, callback=self.parse_item)
    
    def parse_item(self, response): 
        result = ujson.loads(response.body_as_unicode())
        books = result['books']
        book = random.choice(books)
        pprint.pprint(book) 
        item = ItemEntry()
        item['category'] = u'图书'
        item['title'] = book.get('title')
        item['summary'] = book.get('summary')
        item['content'] = book.get('summary')
        item['picOne'] =  book.get('image')
        item['picTwo'] =  book.get('image')
        item['picThr'] =  book.get('image')
        yield item
        
