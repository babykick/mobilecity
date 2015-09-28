from django.contrib import admin
from .models import Location
from .models import POI

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "lat", 'lon']

class POIAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'city', 'bdpoi_id']


admin.site.register(Location, LocationAdmin)
admin.site.register(POI, POIAdmin)