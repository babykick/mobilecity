#coding=utf-8
from django.contrib.gis.db import models as geomodels
from django.db  import models 
from django.contrib.gis.geos import Point, GEOSGeometry
from api.baiduAPI import BaiduMap


 
class BaiduPOIManager(models.Manager):
    def get_queryset(self):
        pass
      
    # 搜索周边
    def search(self, q, loc, radius=1000):
       from .serializers import POISerializer
       pois = BaiduMap.search_distance(q, loc, radius)
       for item in pois['results']:
           # print item
           # print item['name']
           # print item['location']
           uid = item.get('uid')
           # print uid
           info = super(POIManager, self).get_queryset().filter(bdpoi_id=uid)
           if info:
               info = info[0]
               item.update(POISerializer(info).data)
       return pois
       
      
      
class POI(geomodels.Model):
   """ 兴趣点
       based on 百度POI
   """
   # 名称
   name = geomodels.CharField(max_length=100)
      
   # 城市
   city = geomodels.CharField(max_length=20, null=False)
   
   # 坐标
   coordinate = geomodels.PointField(null=True)
   
   # 描述
   description = geomodels.CharField(max_length=200, null=True)
   
   # 投票数
   vote_num = geomodels.IntegerField(default=0)
   
   # 访问频率
   visited_freq = geomodels.IntegerField(default=0)
   
   # 百度POI ID, 返回json中uid项
   bdpoi_id = geomodels.CharField(max_length=25, null=True, unique=True) 
   
   # default manager
   objects = geomodels.GeoManager()
   
   # baidu poi manager，用于merge百度map api poi查询结果和本地数据库查询结果,
   # 返回周边的poi信息
   arounds = BaiduPOIManager() 
    
   def __unicode__(self):
      return self.name

# Create your models here.
class Location(models.Model):
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    description = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=15, null=True)
    
    def __unicode__(self):
      return "%s %s" % (self.lat, self.lon)
   
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    geo = models.OneToOneField(Location, null=True)
    
    
class BaseStation(models.Model):
    site_name = models.CharField(max_length=100)
    cluster = models.CharField(max_length=30)
    geo = models.OneToOneField(Location, null=True)
    