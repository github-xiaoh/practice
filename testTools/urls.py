# -*- coding:utf-8 -*-

from django.conf.urls import url
from testTools import views

urlpatterns = [
    url(r'^userInfo/(?P<page_page>\d+)/$',views.userInfo),
    url(r'^createfilm/$',views.createfilm),
    url(r'^ajaxLogcat/$',views.ajax_logcat),
    url(r'^real_time_log/$',views.real_time_log),
    url(r'ajax_list/$',views.ajax_list),
    url(r'ajax_dict/$',views.ajax_dict),
    url(r'ajax_add/$',views.ajax_add),
    url(r'ajax_req/$',views.ajax_req),
    url(r'special_scene/$',views.special_scene),

]