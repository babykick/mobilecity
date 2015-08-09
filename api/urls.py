from django.conf.urls import url, include
from recommendation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^rcmdlist/$', views.RecommendList.as_view()),
    url(r'^rcmdlist/(?P<pk>[0-9]+)/$', views.RecommendDetail.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

#urlpatterns += static('rcmdlist/static/', document_root=settings.STATIC_ROOT)
