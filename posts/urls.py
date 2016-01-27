#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nabi'

from django.conf.urls import url
from django.contrib import admin

# from .views import (
#     post_list,
#     post_create,
#     post_detail,
#     post_update,
#     post_delete,
#     )

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', "posts.views.post_home"),

    # url(r'^$', post_list),
        # url(r'^posts/$', "<appname>.views.<function_name>"),
        # url(r'^posts/$', posts.views.posts_home ),
        # url(r'^posts/', include("posts.urls")),
    # url(r'^create/$', post_create), #url(r'^create/$', posts.views.post_list ),
    # url(r'^detail/$', post_detail), #url(r'^detail/$', posts.views.post_detail ),
    # url(r'^update/$', post_update), #url(r'^update/$', posts.views.post_update ),
    # url(r'^delete/$', post_delete), #url(r'^delete/$', posts.views.post_delete ),

]