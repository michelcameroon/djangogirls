from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^students$', views.students_list, name='students_list'),
    url(r'^students/(?P<pk>\d+)/detail/$', views.students_detail, name='students_detail'),
    url(r'^students/new/$', views.students_new, name='student_new'),
    url(r'^students/(?P<pk>\d+)/edit/$', views.students_edit, name='students_edit'),
]
