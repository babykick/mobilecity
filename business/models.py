#coding=utf-8
from django.contrib.gis.db import models as geomodels
from django.db  import models 
from django.contrib.gis.geos import Point, GEOSGeometry



class POI(geomodels.Model):
   """ 兴趣点
       based on 百度POI
   """
   # 名称
   name = geomodels.CharField(max_length=100)
     
   # 经纬度
   coordinate = geomodels.PointField(null=True)
   
   # 描述
   description = geomodels.CharField(max_length=200, null=True)
   
   # 投票数
   vote_num = geomodels.IntegerField(default=0)
   
   # 访问频率
   visited_freq = geomodels.IntegerField(default=0)
   
   # 百度POI ID, 返回json中uid项
   bdpoi_id = geomodels.CharField(max_length=25, null=True, unique=True) 
   
   objects = geomodels.GeoManager()
   
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
    