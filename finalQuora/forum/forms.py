from django import forms
from .models import *
import re
from django.contrib.auth import authenticate

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ['heading', 'desc']
	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args,**kwargs)
		self.fields['desc'].required = True

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'desc']
	def __init__(self, *args, **kwargs):
		super(AnswerForm, self).__init__(*args,**kwargs)
		
		
