from django.contrib import admin
from .models import Author
from .auth import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# class TokenInline(admin.StackedInline):
#     model = Token
# 
# class UserAdmin(UserAdmin):
#     inlines = [TokenInline]
#     
 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'mobilephone', 'isAdmin', 'isDeveloper')
    search_fields = ["user__username", "nickname"]

# Automatically create token 
# def author_post_save_receiver(sender, instance, created, **kwargs):
#     if created and instance.isDeveloper:
#         print "Create token for", instance.user.username
#         Token.objects.create(user=instance.user)
# 
# post_save.connect(author_post_save_receiver, sender='users.Author')


@receiver(post_save, sender='users.Author')
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and instance.isDeveloper:
        print "Create token for", instance.user.username
        Token.objects.get_or_create(user=instance.user)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)