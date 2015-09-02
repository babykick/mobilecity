from django.contrib import admin
from .models import RecommendItem
from .models import Comment, Tag


# Register your models here.

# Actions
def make_like_status_hot(modeladmin, request, queryset):
    """
      Make all selected items likeStatus="HOT"
    """
    queryset.update(likeStatus='HOT')
make_like_status_hot.short_description = "Mark like status as HOT"

# Inline 
class TagInline(admin.TabularInline):
    model = Tag
  
# Admin  
class RecommendItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'summary', 'picOne', 'picTwo', 'picThr']
    ordering = ['publishTime']
    actions = [make_like_status_hot]
    inlines = [TagInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'recommendItem')
    
class TagAdmin(admin.ModelAdmin):
    #inlines = [TagInline]
    list_display = ["id", "name", 'recommendItem']
    
admin.site.register(RecommendItem, RecommendItemAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)