from django.contrib import admin
from business.models import GeoEntity

# Register your models here.
class GeoEntityAdmin(admin.ModelAdmin):
    #inlines = [TagInline]
    list_display = ["id", "lat", 'lon']
    
admin.site.register(GeoEntity, GeoEntityAdmin)