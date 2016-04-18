from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=35)
	year = models.IntegerField()

	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Professor(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=35)
	department = models.TextField()
	office = models.TextField()

	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Course(models.Model):
	name = models.CharField(max_length=200)
	number = models.IntegerField()
	department = models.TextField()

	def __unicode__(self):
		return self.name

class Section(models.Model):
	number = models.IntegerField()
	location = models.CharField(max_length=200)
	course = models.ForeignKey(Course)
	professor = models.ForeignKey(Professor)	

	def __unicode__(self):
		return self.name	