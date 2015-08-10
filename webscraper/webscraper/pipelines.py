# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_djangoitem import DjangoItem
import csv
import cStringIO
 
 
class SaveItemToDBPipeline(object):
    def process_item(self, item, spider):
       if isinstance(item, DjangoItem):
            item.save()
            print 'item saved'
       return item  # pass to next pipeline
            
            
class SaveProjectsPipeline(object):
    # use CsvItemExporter
    def __init__(self):
        fields = ['title', 'summary', 'department', 'link', 'pubtime']
        self.csvwriter = csv.DictWriter(open('items_out.csv', 'wb'), fields)
        self.csvwriter.writeheader()
        
    def process_item(self, item, spider):
        if item is not None:
            item = {k: v.encode("gb2312",'ignore') for k,v in item.items()}
            self.csvwriter.writerow(item)
        return item  # pass to next pipeline
            

            