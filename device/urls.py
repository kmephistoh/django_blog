from django.conf.urls import patterns, include, url
from device import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^index$', views.index),
    url(r'^home$', views.device_list),
    url(r'^create/$', views.create_device),
    url(r'^update/$', views.update_device),
)
