from django.conf.urls import url
from recommendation import views

urlpatterns = [
    url(r'^rcmdlist/$', views.RecommendList.as_view()),
    url(r'^rcmdlist/(?P<pk>[0-9]+)/$', views.RecommendDetail.as_view()),
]