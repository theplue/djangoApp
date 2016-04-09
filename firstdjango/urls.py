from django.conf.urls import include, url
from django.contrib import admin

from school import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/index', views.student, name='student'),
    url(r'^professor/index', views.professor, name= 'professor'),
    url(r'^student/(?P<id>\d+)/', views.student_detail, name='student_detail'),
    url(r'^professor/(?P<id>\d+)/', views.professor_detail, name='professor_detail'),
    url(r'^course/index', views.course, name='course'),
    url(r'^course/(?P<id>\d+)/', views.course_detail, name='course_detail'),
   
    url(r'^student/new/$', views.new_student, name='new_student'),
]
