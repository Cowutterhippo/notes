from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view()),
    url(r'^create$', Create.as_view() ),
    url(r'^post/(?P<slug>[\w\-]+$)', BlogDisplayView.as_view()),
    url(r'^edit/(?P<id>[\d]+$)', Edit.as_view()),
    url(r'^api/get$', APIget.as_view())
)
