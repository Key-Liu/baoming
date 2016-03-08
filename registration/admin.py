from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('department_name','department_shortcut','department_number')
	search_fields = ['department_shortcut']

class StudentAdmin(admin.ModelAdmin):
	search_fields = ['student_id','student_name']

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Student_interview)
admin.site.register(Choice)
admin.site.register(Other_interview)