from rest_framework import serializers
from .models import POI, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat',
                  'lon',
                  'city',
                  'description')
        
        
class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ('id',
                  #'name',
                  #'city',
                  #'description',
                  'bdpoi_id',
                  'vote_num'
                  )