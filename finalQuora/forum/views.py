from django.shortcuts import render, redirect, get_object_or_404
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
		return redirect('home');

def answer_form(request, ques_id):
	print("in answer form")
	question = get_object_or_404(Question, pk = ques_id)
	if form.is_valid():
		# question = Question.objects.get(pk=pk)
		ans = form.save(commit = False)
		ans.by = request.user
		# ans_object = Answer.objects.create(question = question)
		ans.ques = question
		ans.save()
		return redirect('home')
	else:
		return redirect('home')
		
		



