from django.shortcuts import render, redirect
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template.response import TemplateResponse
from user.models import MyUser
# Create your views here.
@require_POST
@login_required
def question_form(request):
	form = QuestionForm(request.POST)
	if form.is_valid():
		ques = form.save(commit = False)
		ques.by = request.user
		ques.save()
		return redirect('home');
	else:
		questionform = QuestionForm()
		next = request.GET.get('nexturl')
		return redirect('home');

def answer_form(request):
	if form.is_valid():
		ans = form.save(commit = False)
		ans.by = request.user
		ans.save()
		return redirect('home')
	else:
		return redirect('home');
		
		



