from django.conf.urls import patterns, url
from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', views.article_list, name='home'),
    url(r'^login$', views.login_view),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^article/(?P<id>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^count_like$', views.count_like, name='count_like'),
)
