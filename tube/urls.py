from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.index, name = 'index'),
    url('^today/$',views.index,name='siteToday'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/$',views.search_results,name='search_results'),
    url(r'^video/(?P<vid>\w+)/$',views.video),
    url(r'^new/video$', views.new_video, name='new-video'),
    url(r'^api/merch/$', views.Merchlist.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)