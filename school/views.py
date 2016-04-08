from django.shortcuts import render
from django.http import Http404

from school.models import Student
from school.models import Professor

def index(request):
	studentlist = Student.objects.all()
	context = { 'student_List': studentlist }
	return render(request, 'student/index.html',
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