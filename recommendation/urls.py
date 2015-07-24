from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rcmdlist/$', views.rcmd_list),
    url(r'^rcmdlist/(?P<pk>[0-9]+)/$', views.rcmd_detail),
]