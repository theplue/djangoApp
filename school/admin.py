from django.contrib import admin

from .models import Student, Professor, Course, Section


class StudentAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'year']

admin.site.register(Student, StudentAdmin)

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'office', 'department']

admin.site.register(Professor, ProfessorAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'number', 'department']

admin.site.register(Course, CourseAdmin)

class SectionAdmin(admin.ModelAdmin):
	list_display = ['number', 'location', 'course', 'professor']

admin.site.register(Section, SectionAdmin)

