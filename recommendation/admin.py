from django.contrib import admin
from .models import RecommendItem

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    make_published.short_description = "Mark selected stories as published"
make_published.short_description = "Mark selected stories as published"


class RecommendItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'summary', 'picOne', 'picTwo', 'picThr']
    ordering = ['title']
    actions = [make_published]
admin.site.register(RecommendItem, RecommendItemAdmin)
 