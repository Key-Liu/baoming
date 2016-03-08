# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Department(models.Model):
	department_name = models.CharField(max_length=5,help_text="部门名称")
	department_info = models.CharField(max_length=140,help_text="部门简介",null=True,blank=True)
	department_shortcut = models.CharField(max_length=5,help_text="部门简写")
	department_number = models.IntegerField(help_text="部门面试人数",null=True,blank=True,default=0)

	def __unicode__(self):
		return self.department_name

class Student(models.Model):
	student_id = models.CharField(max_length=12,help_text="学号")
	student_name = models.CharField(max_length=50,help_text="姓名")
	class_num = models.IntegerField(help_text="班级，范围为1-7，7为卓越版")
	doom_num = models.CharField(max_length=10,help_text="宿舍号码",null=True)

	def __unicode__(self):
		return self.student_name

class Choice(models.Model):
	student = models.ForeignKey(Student,help_text="学号")
	first_choice = models.ForeignKey(Department,help_text="第一志愿",related_name="first_choice",null=True)
	second_choice = models.ForeignKey(Department,help_text="第二志愿",related_name="seconde_choide",null=True)

	def __unicode__(self):
		if(self.second_choice):
			return self.student.student_name + "/" + self.first_choice.department_name + "/" + self.second_choice.department_name
		else:
			return self.student.student_name + "/" + self.first_choice.department_name

class Student_interview(models.Model):
	student = models.ForeignKey(Student)
	first_dept = models.ForeignKey(Department,related_name="first_dept",null=True)
	second_dept = models.ForeignKey(Department,related_name="second_dept",null=True)
	first_batch = models.IntegerField(help_text="第一志愿部门面试批次",null=True)
	second_batch = models.IntegerField(help_text="第二志愿部门面试批次",null=True)

	def __unicode__(self):
		if self.second_dept is not None:
			return self.student.student_name + "/" + self.first_dept.department_name + "/" + str(self.first_batch) + "/" + self.second_dept.department_name + "/" + str(self.second_batch)
		else:
			return self.student.student_name + "/" + self.first_dept.department_name + "/" + str(self.first_batch)

class Other_interview(models.Model):
	student = models.ForeignKey(Student)
	first_dept = models.ForeignKey(Department,related_name="other_first_dept",null=True)
	second_dept = models.ForeignKey(Department,related_name="other_second_dept",null=True)
	first_batch = models.IntegerField(help_text="第一志愿部门面试批次",null=True)
	second_batch = models.IntegerField(help_text="第二志愿部门面试批次",null=True)

	def __unicode__(self):
		if self.second_dept is not None:
			return self.student.student_name + "/" + self.first_dept.department_name + "/" + str(self.first_batch) + "/" + self.second_dept.department_name + "/" + str(self.second_batch)
		else:
			return self.student.student_name + "/" + self.first_dept.department_name + "/" + str(self.first_batch)