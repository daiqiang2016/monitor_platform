#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import babyguard.sns.views as views

urlpatterns = [
    url('add_sns$', views.add_sns, name='add_sns'),
    url('get_sns$', views.get_sns, name='get_sns'),
    url('del_sns$', views.del_sns, name='del_sns'),
    url('update_sns$', views.update_sns, name='update_sns'),
    url('reset_all_sns$', views.reset_all_sns, name='reset_all_sns'),
    url('add_comment$', views.add_comment, name='add_comment'),

    #url('get_user_by_user_id$',views.get_user_by_user_id, name='get_user_by_user_id'), 
    #url('login$', views.login, name='login'), 
    #url('modify_password$', views.modify_password, name='modify_password'), 
    #url('modify_user_info$', views.modify_user_info, name='modify_user_info'), 
    #url('register$', views.register, name='register'), 
    #url('register_app_user$', views.register_app_user, name='register_app_user'), 
    #url('reset_password$', views.reset_password, name='reset_password'), 
    #url('send_sms$', views.send_sms, name='send_sms'), 
    #url('clear_all_users$', views.clear_all_users, name='clear_all_users'),
    #url('^test$', views.test, name='test'), 
]
