# -*- encoding: utf-8 -*-
# @Time    : 18-10-17 上午9:21
# @Author  : mike.liu
# @File    : urls.py

from django.conf.urls import url

from webui import web_views

app_name = 'webui'
urlpatterns = [
    url(r'^$', web_views.index, name="index"),

]