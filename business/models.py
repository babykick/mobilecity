#coding=utf-8
from django.contrib.gis.db import models as geomodels
from django.db  import models 

# class POI(models.Model):
#    """ 兴趣点
#        外键到百度POI ID
#    """
#    name = models.CharField(max_length=100)
#    lon = models.FloatField(default=0)
#    lat = models.FloatField(default=0)
#    description = models.CharField(max_length=200, null=True) 
#    vote_num = models.IntegerField(default=0)
#    visited_freq = models.IntegerField(default=0)
#    bdpoi_id = models.CharField(max_length=25, null=True, unique=True) # 百度POI ID, 返回json中uid项

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
    