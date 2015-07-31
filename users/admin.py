from django.contrib import admin
from users.models import Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'mobilephone')

admin.site.register(Author, AuthorAdmin)