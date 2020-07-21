"""HttpRunnerManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from HttpRunnerManager.activator import process
from ApiManager import views as views
from testTools import views as testView
from sc_pay import views as pay_views

urlpatterns = [
    url(r'^userInfo/(?P<page_page>\d+)/',testView.userInfo),
    url(r'^createfilm',testView.createfilm),
    url(r'^account/(?P<page_num>\d+)/',pay_views.account_balance),
    url(r'^admin/', admin.site.urls),
    url(r'^ajaxLogcat/',testView.ajax_logcat),
    url(r'^real_time_log/',testView.real_time_log),
    url(r'ajax_list/',testView.ajax_list),
    url(r'ajax_dict/',testView.ajax_dict),
    url(r'ajax_file/',testView.ajax_file),
    url(r'ajax_add/',testView.ajax_add),
    url(r'ajax_req/',testView.ajax_req),
    url(r'special_scene/',testView.special_scene),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/assets/img/favicon.ico')),
    url('^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    url('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\w+))/$', process),
    url('',views.index),

]
