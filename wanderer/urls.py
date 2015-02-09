from django.conf.urls import patterns, url

from wanderer import views

urlpatterns = patterns('',
  # /
  url(r'^$', views.index, name='index'),
  url(r'^app/$', views.app, name='app'),
  # /1/
  url(r'^(?P<location_id>\d+)/$', views.link, name='redirect'),
)
