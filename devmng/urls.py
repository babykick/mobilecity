#coding=utf-8
from . import views
from django.conf.urls import url

 
urlpatterns = [ url(r'upload', views.upload_file, name='upload'), ]