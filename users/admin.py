from django.contrib import admin
from users.models import Author
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class AuthorInline(admin.StackedInline):
    model = Author

class UserAdmin(UserAdmin):
    inlines = [AuthorInline]
    
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'mobilephone')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)