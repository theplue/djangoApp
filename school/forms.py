from django import forms
from django.forms import ModelForm

from school.models import Student
from school.models import Professor
from school.models import Course

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'year']

class ProfessorForm(ModelForm):
	class Meta:
		model = Professor
		fields = ['first_name', 'last_name', 'office', 'department']

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'number', 'department']