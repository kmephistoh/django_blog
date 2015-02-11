from django.conf.urls import patterns, url
from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^index$', views.index),
    url(r'^home$', views.article_list),
    url(r'^login$', views.login_view),
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
    url(r'^count_like$', views.count_like),
)