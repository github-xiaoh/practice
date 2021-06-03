# -*- coding:utf-8 -*-

from django.conf.urls import url

from user_ch import views

urlpatterns = [
    url(r'^users',views.test_page,name='test_page'),
    url(r'^test_menus/$',views.test_menus,name='test_menus'),
    url(r'^reports',views.test_report,name='test_report'),
    url(r'^ticketcreateinc',views.operation_ticket_create_inc,name='tiicketcreateinc'),
    url(r'^ticketcreatezh',views.operation_ticket_create_zh,name='tiicketcreatezh'),

]
