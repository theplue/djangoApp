from django.shortcuts import render
from django.shortcuts import redirect

from django.http import Http404

from school.models import Student, Section
from school.models import Professor
from school.models import Course

from school.forms import StudentForm
from school.forms import ProfessorForm
from school.forms import CourseForm, SectionForm



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

def new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = StudentForm.save(form)
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})

def new_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = ProfessorForm.save(form)
            return redirect('professor')
    else:
        form = ProfessorForm()
    return render(request, 'professor/professor_form.html', {'form': form})

def new_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = CourseForm.save(form)
            return redirect('course')
    else:
        form = ProfessorForm()
    return render(request, 'course/course_form.html', {'form': form})

def new_section(request):
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            section = SectionForm.save(form)
            return redirect('index')
    else:
        form = SectionForm()
    return render(request, 'section/section_form.html', {'form': form})