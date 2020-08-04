# -*- coding:utf-8 -*-

from django.conf.urls import url
from sc_pay import views

urlpatterns = [
    url(r'^account/(?P<page_num>\d+)/$',views.account_balance,name='account'),

]