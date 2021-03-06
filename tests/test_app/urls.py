# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

from test_app.views import TestView1, TestView2, TestView3

urlpatterns = patterns('',
    url(r'^test1/$', TestView1.as_view(), name='test-home'),
    url(r'^test2/$', TestView2.as_view(), name='test-home2'),
    url(r'^test3/$', TestView3.as_view(), name='test-home3'),
)
