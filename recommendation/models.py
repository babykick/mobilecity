#coding=utf-8
from django.db import models
from django.conf import settings
#from django.contrib.sites.models import Site
# Create your models here.

class RecommendItem(models.Model):
    # 推荐标题
    title = models.CharField(max_length=50, default="")
    # 摘要
    summary = models.CharField(max_length=100, default="")
    # 内容
    content = models.CharField(max_length=100, default="")
    # 评论
    comment = models.CharField(max_length=100, default="")
    # 图片列表字符串 
    picListString = models.CharField(max_length=100, default="")
    # 图片1 URL 
    picOne = models.CharField(max_length=100, default="")
    # 图片2 URL 
    picTwo = models.CharField(max_length=100, default="")
    # 图片3 URL 
    picThr = models.CharField(max_length=100, default="")
    # 图片 列表 
    picList = models.CharField(max_length=100, default="")
    # 图片类型是否为大图 
    isLarge = models.CharField(max_length=100, default="")
    # 阅读状态 ，读过的话显示灰色背景 
    readStatus = models.CharField(max_length=100, default="")
    # 收藏状态 
    collectStatus = models.CharField(max_length=50, default="")
    # 喜欢 状态 
    likeStatus = models.CharField(max_length=50, default="")
    # 感兴趣状态 
    interestedStatus = models.CharField(max_length=50, default="")
    
    
    def hotestComment():
        return ""
    
    def absoluteImageUrl(self, imgname):
        return 'http://111.8.186.228:8000%s%s' % (settings.IMAGE_URL, imgname)
    
     
    def _picOneURL(self):
        return self.absoluteImageUrl(self.picOne)
    
    def _picTwoURL(self):
        return self.absoluteImageUrl(self.picTwo)
    
    # Additional properties
    picOneURL = property(_picOneURL)
    picTwoURL = property(_picTwoURL)
    
    