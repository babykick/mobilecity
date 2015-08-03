#coding=utf-8
from django.db import models
from django.conf import settings
from users.models import Author
#from django.contrib.sites.models import Site
# Create your models here.
from django.utils.timezone import localtime
from business.models import GeoEntity

class RecommendItem(models.Model):
    # 推荐标题
    title = models.CharField(max_length=500)
    # 摘要
    summary = models.CharField(max_length=500, default="",blank=True)
    # 内容
    content = models.CharField(max_length=1000, default="")
    # 评论
    # "comments" rative_name from Comment
    # 图片列表字符串 
    picListString = models.CharField(max_length=100, default="",blank=True)
    # 图片1 URL 
    picOne = models.CharField(max_length=100, default="",blank=True)
    # 图片2 URL 
    picTwo = models.CharField(max_length=100, default="",blank=True)
    # 图片3 URL 
    picThr = models.CharField(max_length=100, default="",blank=True)
    # 图片 列表 
    picList = models.CharField(max_length=100, default="",blank=True)
    # 图片类型是否为大图 
    isLarge = models.CharField(max_length=100, default="",blank=True)
    # 阅读状态 ，读过的话显示灰色背景 
    readStatus = models.CharField(max_length=100, default="",blank=True)
    # 收藏状态 
    collectStatus = models.CharField(max_length=50, default="",blank=True)
    # 喜欢 状态 
    likeStatus = models.CharField(max_length=50, default="",blank=True)
    # 感兴趣状态 
    interestedStatus = models.CharField(max_length=50, default="",blank=True)
    
    # 发布时间 UTC
    publishTime = models.DateTimeField( auto_now=True, null=True)
    
    # 作者
    author = models.ForeignKey(Author, verbose_name="author for the recommendation",
                               related_name="recommendations", null=True)
    
    # 地理位置
    geo = models.OneToOneField(GeoEntity, null=True, blank=True)
    
    def LocalPublishtime(self):
        if self.publishTime is not None:
            return localtime(self.publishTime)
        return self.publishTime
    
    def hotestComment(self):
        return ""
    
    
    def absoluteImageUrl(self, imgname):
        if imgname.startswith('http'):
            return imgname
        return 'http://111.8.186.228:8000/static/images/%s' % imgname   
    
     
    def picOneURL(self):
        return self.absoluteImageUrl(self.picOne)
    
    def picTwoURL(self):
        return self.absoluteImageUrl(self.picTwo)
    
    def picThrURL(self):
        return self.absoluteImageUrl(self.picThr)
    
    
    # Additional properties
    picOneURL = property(picOneURL)
    picTwoURL = property(picTwoURL)
    picThrURL = property(picThrURL)
    LocalPublishtime = property(LocalPublishtime)
    
    
    def __unicode__(self):
        return "%s %s" % (self.id, self.title)
    
    
    class Meta:
        #ordering = ["publishTime"]
        pass
    
    
class Comment(models.Model):
     content = models.CharField(max_length=500)
     author = models.ForeignKey(Author, verbose_name="comment author", related_name="comments", null=True)
     recommendItem = models.ForeignKey(RecommendItem, verbose_name="recommend item", related_name="comments", null=True)
     # 发布时间 UTC
     publishTime = models.DateTimeField(auto_now_add=True, null=True)
     
     def LocalPublishtime(self):
        if self.publishTime is not None:
            return localtime(self.publishTime)
        return self.publishTime