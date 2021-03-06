from django.conf.urls import url, include
from recommendation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^rcmdlist/$', views.RecommendList.as_view()),
    url(r'^rcmdlist/(?P<pk>[0-9]+)/$', views.RecommendDetail.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentList.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^poi/', include('business.urls')),
   
]

#urlpatterns += static('rcmdlist/static/', document_root=settings.STATIC_ROOT)
