import scrapy

class OilItem(scrapy.Item):
    price = scrapy.Field()
    date = scrapy.Field()
    