from django.contrib import admin
from .models import Author
from .auth import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# class TokenInline(admin.StackedInline):
#     model = Token
# 
# class UserAdmin(UserAdmin):
#     inlines = [TokenInline]
#     
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'mobilephone')
    search_fields = ["user__username","nickname"]

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)