# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,  logout
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *;

# 主页
def index_view(request):
	# 如果已经登入
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('registration:input'))
	# 未登入
	# c = {}
	# c.update(csrf(request))
	# 这两行是跨站请求伪造保护，保证网站不接受跨站请求
	else:
		c = {}
		c.update(csrf(request))
		return render_to_response("registration/login.html", c)

# 用户登入请求
def login_view(request):
	# 使用Django自带的Authentication system
	username = request.POST['username']
	password = request.POST['password']
	idclass = request.POST['idclass']
	user = authenticate(username=username,password=password)
	# 干事用户
	if idclass == "staff":
		if user is not None:
			if user.is_active:
				# 把该用户加入Session
				login(request, user)
				return HttpResponseRedirect(reverse('registration:input'))
			else:
				return HttpResponse("disabled account!")
		else:
			return HttpResponse("用户密码错误或者用户不存在！")
	# 管理员用户
	if idclass == "admin":
		if user is not None:
			if user.is_active:
				if user.is_staff:
					# 把该用户加入Session
					login(request, user)
					return HttpResponseRedirect(reverse('admin_manage:index'))
				else:
					return HttpResponse("disabled account!")
			else:
				return HttpResponse("disabled account!")
		else:
			return HttpResponse("用户密码错误或者用户不存在！")

# 录入界面
def input_view(request):
	# 确保用户已经登入
	# c = {}
	# c.update(csrf(request))
	# 这两行是跨站请求伪造保护，保证网站不接受跨站请求
	if request.user.is_authenticated():
		c = {}
		c.update(csrf(request))
		return render_to_response("registration/input.html", c)
	# 用户未登入
	else:
		return HttpResponse("您当前未登入")

# 登出请求
def logout_view(request):
	# 从Session中移除该用户，既登出
	logout(request)
	return HttpResponseRedirect(reverse('registration:index'))

# 根据学号获取Student对象并返回json数据
@csrf_exempt
def get_stu_view(request):
	if request.user.is_authenticated():
		try:
			stu_id = request.POST['stu_id']
			stu_object = Student.objects.get(student_id=stu_id)
			stu_name = stu_object.student_name
			class_num = stu_object.class_num
			doom_num = stu_object.doom_num
			# 返回值
			return_value ={
			"stu_name":stu_name,
			"class_num":class_num,
			"doom_num":doom_num
			}
			return HttpResponse(json.dumps(return_value))

		except Exception,ex:
			return HttpResponse()
	else:
		return HttpResponse("您当前未登入")

# 录入一名学生
@csrf_exempt
def add_stu_view(request):
	if request.user.is_authenticated():
		try:
			stu_id = request.POST['stu_id']
			first_choice_shortcut = request.POST['first_choice']
			second_choice_shortcut = request.POST['second_choice']
			student = Student.objects.get(student_id=stu_id)
			get_choice_list = Choice.objects.filter(student=student)
			# 判断该学生是否已录入
			if(len(get_choice_list) == 0):
				# 第二志愿为空时
				if(second_choice_shortcut == ""):
					first_choice = Department.objects.get(department_shortcut=first_choice_shortcut)
					new_choice = Choice(student=student,first_choice=first_choice)
					new_choice.save()
				# 第二志愿不为空时
				else:
					first_choice = Department.objects.get(department_shortcut=first_choice_shortcut)
					second_choice = Department.objects.get(department_shortcut=second_choice_shortcut)
					new_choice = Choice(student=student,first_choice=first_choice,second_choice=second_choice)
					new_choice.save()
				return HttpResponse("添加成功！")
			else:
				return HttpResponse("已存在相同学号的记录！")
		except Exception,ex:
			return HttpResponse(Exception)
	else:
		return HttpResponse("您当前未登入")
