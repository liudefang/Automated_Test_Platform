# -*- encoding: utf-8 -*-
# @Time    : 18-10-17 上午9:21
# @Author  : mike.liu
# @File    : urls.py
from django.conf.urls import url
from appui import app_views

app_name = 'appui'
urlpatterns = [
    url(r'^$', app_views.index, name="index"),

]