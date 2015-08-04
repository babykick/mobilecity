#from django.contrib.gis.db import models as geomodels
from django.db  import models 
 
# Create your models here.
class GeoEntity(models.Model):
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    description = models.CharField(max_length=200, null=True) 
    
    
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    geo = models.OneToOneField(GeoEntity, null=True)
    
    
class BaseStation(models.Model):
    site_name = models.CharField(max_length=100)
    cluster = models.CharField(max_length=30)
    geo = models.OneToOneField(GeoEntity, null=True)
    