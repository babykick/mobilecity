from scrapy.item import Item
import scrapy

class BaseItem(Item):
    name = scrapy.Field()
    comments_cnt = scrapy.Field()
    pic_thumb = scrapy.Field()
    
class DzdpItem(BaseItem):
    pass

