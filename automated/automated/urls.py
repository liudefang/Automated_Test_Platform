"""automated URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


from api import urls
from test_platform import views
from api import api_views
from appui import app_views
from  webui import web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^index/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^home/$', views.home),

    # 项目
    url(r'^project/$', views.project),
    url(r'^add_project/$', views.add_project),
    url(r'^del_project/$', views.del_project),

    # 模块
    url(r'^modules/$', views.modules),
    url(r'^add_modules/$', views.add_modules),

    url(r'^toastr/$', views.toastr),

    # api子路由
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
    # appui子路由
    url(r'^appui/', include('appui.urls', namespace='appui', app_name='appui')),
    # webui子路由
    url(r'^webui/', include('webui.urls', namespace='webui', app_name='webui')),
]
