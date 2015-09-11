from django.contrib import admin
from business.models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    #inlines = [TagInline]
    list_display = ["id", "lat", 'lon']
    
admin.site.register(Location, LocationAdmin)