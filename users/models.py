#coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    """
       User field has:
            username
            password
            email
            first_name
            last_name
    """
    # 昵称
    nickname = models.CharField(max_length=50)
    
    # 手机号码
    mobilephone = models.CharField(max_length=30)
    
    # to User model for auth
    userAuth = models.OneToOneField(User, null=True)
    
    # 头像
    avatar = models.CharField(max_length=100, null=True)
    
    # 等级
    level = models.IntegerField(default=1)
    
    # 家乡
    hometown = models.CharField(max_length=20, null=True)
    
    # 是否本地人(判断口味特点)
    isLocal = models.BooleanField(default=False)
    
    # 是否管理员
    isAdmin = models.BooleanField(default=False)
    
    # 是否开发者
    isDeveloper = models.BooleanField(default=False)
    
    #是否掌柜
    isShopkeeper = models.BooleanField(default=False)
    
    # 返回用户名
    @property
    def username(self):
        return self.user.username
    
    def __unicode__(self):
        return self.user.username
    