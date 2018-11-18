# -*- encoding: utf-8 -*-
# @Time    : 18-10-17 上午9:21
# @Author  : mike.liu
# @File    : urls.py

from django.conf.urls import url

from api import api_views

app_name = 'api'
urlpatterns = [
    url(r'^$', api_views.index, name="index"),
    url(r'^apitest_manage/$', api_views.apitest_manage, name="apitest_manage"),
    url(r'^apistep_manage/$', api_views.apistep_manage, name="apistep_manage"),


]