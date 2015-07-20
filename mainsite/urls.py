#coding=utf-8
from . import views
from django.conf.urls import url

# For this site 
urlpatterns = [ url(r'^$', views.index, name='index'), ]