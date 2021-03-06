"""
Definitions of different models used in livelatex.

.. moduleauthor:: Jain Basil Aliyas <jainbasil@gmail.com>

""" 

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from server.settings import INPUT_FILE_TYPES, OUTPUT_FILE_TYPES

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	is_active = models.BooleanField()
	activation_key = models.CharField(max_length=40)
	key_expires = models.DateTimeField()
	
class Project(models.Model):
	"""
	This module defines a project in LiveLaTeX.
	"""
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	short_name = models.CharField(max_length=32)
	long_name = models.CharField(max_length=64)
	description = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.short_name
	
class File(models.Model):
	"""
	This module define a file in a project. This will
	reside in the Project as many-to-one relationship
	"""
	project = models.ForeignKey(Project)
	file_name = models.CharField(max_length=32)
	file_type = models.CharField(max_length=5, choices=INPUT_FILE_TYPES)
	created = models.DateTimeField()
	modified = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	
	def __unicode__(self):
		return self.file_name

