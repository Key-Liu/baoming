from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index_view,name="index"),
	url(r'^compute$',views.compute_view,name="compute"),
	url(r'^calculate$',views.calculate_view,name="calculate"),
	url(r'^show$',views.show_view,name="show"),
	url(r'^check_overlap$',views.check_overlap_view,name="check_overlap"),
	url(r'^overlap$',views.overlap_view,name="overlap"),
	url(r'^count$',views.count_view,name="count"),
	url(r'^change_time$',views.check_time_view,name="change_time"),
	url(r'^get_student_interview$',views.get_stu_inter_view,name="get_student_interview"),
	url(r'^save_student_interview$',views.save_stu_inter_view,name="save_student_interview"),
	url(r'^export_doc$',views.export_doc_view,name="export_doc"),
	url(r'^export_page$',views.export_page_view,name="export_page")
]