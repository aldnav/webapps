from django.conf.urls import patterns, url
from fighter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<fighter_slug>[-\w]+),(?P<fighter_id>\d+)/$', views.detail, name='fighter_detail'),
)