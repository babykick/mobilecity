# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
import cStringIO
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
from scrapy_djangoitem import DjangoItem
from scrapy.utils.project import get_project_settings
from webscraper.items import ProjectItem, DocItem

 
 
class SaveItemToDBPipeline(object):
    def process_item(self, item, spider):
       if isinstance(item, DjangoItem):
            item.save()
            print 'item saved'
       return item  # pass to next pipeline
            
            
class SaveProjectsInfoPipeline(object):
    # use CsvItemExporter
    def __init__(self):
        fields = ['rank', 'pubtime', 'title', 'summary', 'department', 'link']
        self.csvwriter = csv.DictWriter(open('items_out.csv', 'wb'), fields)
        self.csvwriter.writeheader()
        
    def process_item(self, item, spider):
        if isinstance(item, ProjectItem):
            item = {k: v.encode("gb2312",'ignore') for k,v in item.items()}
            self.csvwriter.writerow(item)
        return item  # pass to next pipeline
            
            
class DownloadProjectDocsPipeline(FilesPipeline):
    """ Save file pipeline
    """
  
    def get_media_requests(self, item, info):
        if isinstance(item, DocItem):
            for finfo in item['file_urls']:
                yield Request(url=finfo['url'], meta={"file_name": finfo['fname']})
           
                
    def file_path(self, request, response=None, info=None):
        return request.meta["file_name"] 
    
    
    # def item_completed(self, results, item, info):
    #     pass
    #     #return item
        