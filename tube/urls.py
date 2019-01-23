from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.welcome, name = 'welcome'),
    url('^today/$',views.welcome,name='siteToday'),
    url('^search/$',views.search_results,name='search_results'),
    url(r'^new/video$', views.new_video, name='new-video')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)