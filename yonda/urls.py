#-*- coding:utf-8 -*-
from yonda.models import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('yonda.views',
    url(r'^$', 'index', name='index'),
    url(r'^signup$', 'signup', name='signup'),
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^timeline$', 'timeline', name='timeline'),
    url(r'^user/(?P<username>.*)$', "user_timeline", name="user_timeline"),
)

