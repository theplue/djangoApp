from django import forms
from django.forms import ModelForm

from school.models import Student, Professor, Course, Section

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

class SectionForm(ModelForm):
	class Meta:
		model = Section
		fields = ['number', 'location', 'course', 'professor']