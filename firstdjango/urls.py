from django.conf.urls import include, url
from django.contrib import admin

from school import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/index', views.index, name='student'),
    url(r'^professor/index', views.professor, name= 'professor'),
    url(r'^student/(?P<id>\d+)/', views.student_detail, name='student_detail'),
    url(r'^professor/(?P<id>\d+)/', views.professor_detail, name='professor_detail'),
]
