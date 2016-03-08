# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页页面
	url(r'^$',views.index_view,name="index"),
	# 登入请求               
	url(r'^login$',views.login_view,name="login"), 
	# 录入页面         
	url(r'^input$',views.input_view,name="input"), 
	# 登出         
	url(r'^logout$',views.logout_view,name="logout"),	
	# 获取Student	
	url(r'^get_stu$',views.get_stu_view,name="get_stu"),
	# 添加Student	
	url(r'^add_stu$',views.add_stu_view,name="add_stu"),	
]