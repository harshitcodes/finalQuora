from django.db import models
from user.models import *
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 200, blank = True)
	related_pic = models.ImageField(upload_to = 'Topic_Pics/', blank = True)

	
	def __str__(self):
	  return self.name

class Question(models.Model):
	heading = models.TextField(max_length = 500)
	desc = models.TextField(max_length = 1000, blank = True)
	topic = models.ManyToManyField(Topic, related_name = 'related_topic')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	by = models.ForeignKey(MyUser, related_name = 'questions_uploaded')
	views = models.ForeignKey(MyUser,related_name = 'questions_viewed', null = True)
	def __str__(self):
	  return self.heading
	

class Answer(models.Model):
	text = models.TextField(max_length = 10000)
	desc = models.TextField(max_length = 50, blank = True, verbose_name = 'Description')
	ques = models.ForeignKey(Question)
	by = models.ForeignKey(MyUser)	
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	views = models.ForeignKey(MyUser, related_name = 'a_MyUser', null = True)

	def __str__(self):
	  return self.desc
