#coding=utf-8
from django.db import models
from django.conf import settings
from users.models import Author
#from django.contrib.sites.models import Site
# Create your models here.
from django.utils.timezone import localtime
from business.models import GeoEntity
from django.db.models import Max
from datetime import datetime 
from django.utils import timezone

class RecommendItem(models.Model):
    CATEGORY_CHOICES = (
        ('WESTFOOD', u'西餐'),
        ('CHINESEFOOD', u'中餐'), 
    )
    
    # 推荐标题
    title = models.CharField(max_length=500)
    
    # 摘要
    summary = models.CharField(max_length=500, default="",blank=True)
    
    # 内容
    content = models.CharField(max_length=1000, default="")
  
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
    
    # 类别
    category = models.CharField(max_length=20, null=True, blank=True)
    
    # 发布时间 UTC
    publishTime = models.DateTimeField(auto_now_add=True, null=True)
    # 作者
    author = models.ForeignKey(Author, verbose_name="author for the recommendation",
                               related_name="recommendations", null=True, default=1) # Default is the supper user(id=1)
    # 获赞数
    upCount = models.IntegerField(default=0)
    # 获贬数
    downCount = models.IntegerField(default=0)
    # 地理位置
    geo = models.OneToOneField(GeoEntity, null=True, blank=True)
    
    # 评论 rative_name from Comment
    """self.comments"""
    
     # 标签 rative_name from Tag
    """self.tags"""
    # 发布时间
    @property
    def localPublishTime(self):
        if self.publishTime is not None:
            return localtime(self.publishTime).strftime("%Y-%m-%d %H:%M:%S")
        return self.publishTime
    
    # 发布已过去的时间
    @property
    def pubElapse(self):
        """
           刚刚：1小时内
           一周前：7天前
        """
        elapse = datetime.now(timezone.utc) - self.publishTime 
        if elapse.days >= 7:
            return u'一周前'
        else:
            if elapse.days >= 1:
                return u'最近'
            return u"刚刚"
           
        
    # 最近的评论
    @property
    def latestComments(self):
        return self.comments.all().order_by('-publishTime')[:1]
    
    @property
    def commentCount(self):
        return self.comments.all().count()
    
    # 最热的评论（获赞数最多的）
    @property
    def hotestComment(self):
        maxUpCount = self.comments.all().aggregate(Max('upCount'))['upCount__max']
        if maxUpCount > 0:
            return self.comments.all().get(upCount=maxUpCount).content
          
    # 作者的名字
    @property
    def authorName(self):
        return self.author.nickname
    
    # 图片url 
    def absoluteImageUrl(self, imgname):
        if imgname.startswith('http'):
            return imgname
        return 'http://111.8.186.228:8000/static/images/%s' % imgname   
    
    # picOne url
    @property 
    def picOneURL(self):
        return self.absoluteImageUrl(self.picOne)
    
    # picTwo url
    @property
    def picTwoURL(self):
        return self.absoluteImageUrl(self.picTwo)
    
    # picThr url
    @property
    def picThrURL(self):
        return self.absoluteImageUrl(self.picThr)
    
    # 头像
    @property
    def avatar(self):
        return self.author.avatar
    
    
    def __unicode__(self):
        return "#%s %s" % (self.id, self.title)
    
    
    class Meta:
        #ordering = ["publishTime"]
        get_latest_by = 'publishTime'
    
    
    
class Comment(models.Model):
     """
         Comments
     """
     # 内容
     content = models.CharField(max_length=500)
     # 作者
     author = models.ForeignKey(Author, verbose_name="comment author", related_name="comments", null=True, default=1)
     # 推荐项
     recommendItem = models.ForeignKey(RecommendItem, verbose_name="recommend item", related_name="comments", null=True)
     # 发布时间 UTC
     publishTime = models.DateTimeField(auto_now_add=True, null=True)
     # 获赞数
     upCount = models.IntegerField(default=0)
     # 获贬数
     downCount = models.IntegerField(default=0)
     
     # 本地发布时间
     @property
     def localPublishTime(self):
        if self.publishTime is not None:
            return localtime(self.publishTime).strftime("%Y-%m-%d %H:%M:%S")
        return self.publishTime
    
     class Meta:
        ordering = ["publishTime"]
        get_latest_by = 'publishTime'
    
    
class Tag(models.Model):
    name = models.CharField(max_length=30)
     # 推荐项
    recommendItem = models.ForeignKey(RecommendItem, verbose_name="recommend item", related_name="tags", null=True)