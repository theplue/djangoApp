from django.shortcuts import render
from django.http import Http404

from school.models import Student

def index(request):
	studentlist = Student.objects.all()
	context = { 'student_List': studentlist }
	return render(request, 'student/index.html',
		context )

def item_detail(request, id):
	try:
		student = Student.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This student does not exist')
	return render(request, 'Student/student_detail.html', {
		'student': student,
	})