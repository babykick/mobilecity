#coding=utf-8
from django.db import models
from django.conf import settings
from users.models import Author
#from django.contrib.sites.models import Site
# Create your models here.
from django.utils.timezone import localtime
from business.models import Location
from django.db.models import Max
from datetime import datetime 
from django.utils import timezone
from business.models import POI
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericRelation
from cloudinary.models import CloudinaryField 




class Comment(models.Model):
     """
         Comments
     """
     # 内容
     content = models.CharField(max_length=500)
     
     # 作者
     author = models.ForeignKey(Author, verbose_name="comment author", related_name="comments", null=True, default=1)
     
     # 推荐项
     #recommendItem = models.ForeignKey(RecommendItem, verbose_name="recommend item", related_name="comments", null=True)
     
     # 评论关联对象外键，因为可以评论多种对象，所以使用泛型
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
     object_id = models.PositiveIntegerField(null=True)
     content_object = GenericForeignKey('content_type', 'object_id') # 用这个field赋值
     
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
    # 标签名称
    name = models.CharField(max_length=30)
    
    # generic relative, 可标签到不同对象
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
     
 

class AroundManager(models.Manager):
    """ 搜索附近的用户推荐项目
    """
    def search(self, point, dist=1000):
        """ point: 中心点坐标 tuple (lat, png)
            dist: 到中心点距离
        """
        if not isinstance(point, Point):
            point = Point(point)
        return super(ArroundManager, self).get_queryset().filter(coordinate__distance_lte=(point, dist))
      
      

class RecommendItem(geomodels.Model):
    CATEGORY_CHOICES = (
        (u'美食', u'美食'),
        (u'服装', u'服装'),
        (u'数码', u'数码'),
        (u'图书', u'图书'),
    )
     
    # 相关的POI id， 可选项，UGC的项目不一定是注册的POI
    poi = models.ForeignKey(POI, related_name="recommendations", blank=True, null=True)
    
    # 坐标
    coordinate = geomodels.PointField(null=True)
    
    # 推荐标题
    title = models.CharField(verbose_name=u"标题", max_length=500)
    
    # 摘要
    summary = models.CharField(max_length=500, default="",blank=True)
    
    # 内容介绍
    content = models.CharField(max_length=1000, default="")
    
    # 图片field
    #mainImage = models.ImageField(verbose_name="main_image", default="", blank=True)
    
    # 云图
    cloudImage = CloudinaryField('cloud_image', blank=True, null=True)
    
    # 图片1 URL 
    picOne = models.CharField(max_length=100, default="",blank=True)
    
    # 图片2 URL 
    picTwo = models.CharField(max_length=100, default="",blank=True)
    
    # 图片3 URL 
    picThr = models.CharField(max_length=100, default="",blank=True)
    
    # 图片 列表 
    picList = models.CharField(max_length=100, default="",blank=True)
    
    # 阅读状态 ，读过的话显示灰色背景 
    readStatus = models.CharField(max_length=100, default="",blank=True)
    
    # 收藏状态 
    collectStatus = models.CharField(max_length=50, default="",blank=True)
    
    # 喜欢 状态 
    likeStatus = models.CharField(max_length=50, default="",blank=True)
    
    # 感兴趣状态 
    interestedStatus = models.CharField(max_length=50, default="",blank=True)
    
    # 类别
    category = models.CharField(max_length=20, null=True, blank=True,  choices=CATEGORY_CHOICES)
    
    # 发布时间 UTC
    publishTime = models.DateTimeField(auto_now_add=True, null=True)
    
    # 作者
    author = models.ForeignKey(Author, verbose_name="author for the recommendation",
                               related_name="recommendations", null=True, default=1) # Default is the supper user(id=1)
    # 获赞数
    upCount = models.IntegerField(default=0)
    
    # 获贬数
    downCount = models.IntegerField(default=0)
    
    # default manager
    objects = geomodels.GeoManager()
    
    # around manager
    around = AroundManager()
   
    # 评论 relative
    comments = GenericRelation(Comment,
                               related_query_name='recommends'
                               )
    
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
    
   