from django.shortcuts import render
from django.http import Http404

from school.models import Student
from school.models import Professor
from school.models import Course

def index(request):
	return render(request, 'base.html' )

def student(request):
	studentlist = Student.objects.all()
	context = { 'student_List': studentlist }
	return render(request, 'student/student.html',
		context )

def student_detail(request, id):
	try:
		student = Student.objects.get(id=id)
	except Student.DoesNotExist:
		raise Http404('This student does not exist')
	return render(request, 'Student/student_detail.html', {
		'student': student,
	})

def professor(request):
	professorlist = Professor.objects.all()
	context = { 'professor_List': professorlist }
	return render(request, 'professor/professor.html',
		context )

def professor_detail(request, id):
	try:
		professor = Professor.objects.get(id=id)
	except Professor.DoesNotExist:
		raise Http404('This professor does not exist')
	return render(request, 'professor/professor_detail.html', {
		'professor': professor,
	})

def course(request):
	courseList = Course.objects.all()
	context = {'courseList': courseList }
	return render(request, 'course/course.html', context )

def course_detail(request, id):
	try:
		course = Course.objects.get(id=id)
	except course.DoesNotExist:
		raise Http404('This course does not exist')
	return render(request, 'course/course_detail.html', {
		'course': course,
	})



