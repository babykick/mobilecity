from django.contrib.gis.db import models  
 
 
# Create your models here.
class GeoModel(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    objects = models.GeoManager()
    
    class Meta:
        abstract = True
    
class Shop(GeoModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

class BaseStation(GeoModel):
    site_name = models.CharField(max_length=100)
    
    cluster = models.CharField(max_length=30)
    