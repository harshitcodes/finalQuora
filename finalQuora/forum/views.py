from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template.response import TemplateResponse
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse, JsonResponse
from user.models import MyUser
from .models import Question, Answer
from django.db.models import Q
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


@login_required
@require_http_methods(['GET', 'POST'])
def add_answer(request, ques_id = None):
	print("in answer form")
	question = get_object_or_404(Question, id = ques_id)
	if request.method == 'GET':
		form = AnswerForm()
		print("get add answer method")
	else:
		
		answer_text = request.POST.get('answers')
		if answer_text:
			answer = Answer.objects.create(
				ques = question,
				by = request.user,
				text = answer_text
				);
			answer.save()
			if answer:
				print (answer.text)
			else:
				print("Answer not found")
			return JsonResponse({'success': 1, 'answer': {'id': answer.id, 'text': answer.text} });

	return render(request, 'forum/addanswer.html', {'form' : form, 'ques_id' : question.id})	

		



