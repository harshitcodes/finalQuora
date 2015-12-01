from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# using built in password reset below...
from django.contrib.auth.views import password_reset, password_reset_confirm
from .models import MyUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.core import serializers
from django.core.mail import EmailMessage
from .forms import *
import datetime
import base64
import json
from .models import *
from forum.models import *
from forum.forms import *
from django.db.models import Q
#from .forms import NameForm, ContactForm, LocationForm

# Create your views here.

@require_GET
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return redirect('login')

def hello(request):
	signupform = SignUpForm()
	return render(request, 'user/signup_form.html',{'signupform': signupform})
# def postsignup(request):
# 	return render(request, 'user/postsignup.html')
@require_GET
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    next_url = request.GET.get('next')
    signupform = SignupForm()
    loginform = LoginForm()
    data = { 'loginform' : loginform, 'signupform' : signupform, 'next' : next_url }
    return render(request, 'user/base.html', data);

@require_http_methods(["GET", "POST"])
def signup_form(request):
	if request.user.is_authenticated():
		return redirect('home')
	form = SignUpForm(request.POST)
	if form.is_valid():
		user = form.save()
		user.is_active = False
		user.save();
		url = request.build_absolute_uri(reverse('activate'));
		url = url + "?user=" + base64.b64encode(user.username.encode('utf-8')).decode('utf-8')
		message = '''Welcome! {{user.username}} to MyQuora. Click <a href = "%s">here </a> to activate your account ''' % url
		email = EmailMessage('Welcome', message, to=[user.email])
		email.send()
		return render(request, 'user/postsignup.html', {'user': user})

	else:
		signupform = form
		loginform = LoginForm()
		nexturl = request.GET.get('next')
		data = { 'loginform' : loginform, 'signupform' : signupform, 'next' : nexturl }
		return render(request, 'user/base.html', data);    

@require_GET
def activateaccount(request):
	if request.user.is_authenticated():
		return redirect('home')
	username = base64.b64decode(request.GET.get('user').encode('utf-8').decode('utf-8'))
	user = get_object_or_404(MyUser, username = username)
	user.is_active = True
	user.save()
	return render(request, 'user/base.html', {'loginform':LoginForm(), 'act': True})	


@require_http_methods(['GET', 'POST'])
def login_form(request):
	if request.user.is_authenticated():
		return redirect('home')
	f = LoginForm(request.POST)
	nexturl = request.POST.get('next')
	if f.is_valid():
		user = f.get_user();
		login(request, user);
		if not nexturl:
			return redirect('home')
		else:
			return redirect(nexturl)
	else:
		loginform = f
		signupform = SignUpForm()
		data = { 'loginform' : loginform, 'signupform' : signupform , 'next' : nexturl }
		return render(request, 'user/base.html', data);

@require_GET
@login_required
def home(request):
	user_list = MyUser.objects.all()
	all_users = MyUser.objects.filter(~Q(id = request.user.id), is_active = True)
	questions = request.user.questions_uploaded.all();
	# including answers.
	# views = MyUser.objects.filter(~Q( id = request.user.id), questions_viewed.all())
	answers = Answer.objects.all()
	questionform = QuestionForm()
	answerform = AnswerForm()
	data = {'user_list': user_list, 'users':all_users, 'questionform': questionform,
	'questions':questions, 'answerform': answerform, 'answers':answers}
	return render(request, 'user/home.html',data)

@require_GET
@login_required
def write_answer(request, id):
	quesid = get_object_or_404(Question, pk = id)
	context = {'ques': ques}
	return render(request, 'user/home.html', context)

@require_GET
@login_required
def otherhome(request):
    all_users = MyUser.objects.filter(~Q(id = request.user.id), is_active = True)
    return render(request, 'user/otherhome.html', {'user_list' : all_users});

@require_GET
def logoutview(request):
	logout(request)
	return redirect('login_form')

def reset(request):
	return password_reset(request, template_name = 'user/reset.html',
		email_template_name = 'user/reset_email.html',
		subject_template_name = 'user/reset_subject.txt',
		post_reset_redirect = reverse('password_reset_request'))

def reset_confirm(request, uidb64 = None, token = None):
	return password_reset_confirm(request,
		template_name = 'user/reset.html',
		uidb64 = uidb64	,
		token = token,
		post_reset_redirect = reverse('success'))

def success(request):
	return render(request, 'user/success.html')

def password_reset_request(request):
	return render(request, 'user/initiated_password_request')


@require_GET
@login_required
def follow(request, id):
	followee = get_object_or_404(MyUser, id = id)
	follower = request.user
	response_data = {'result': 0}
	if followee.id != follower.id and followee not in follower.following.all():
		follower.following.add(followee)
		response_data['result'] = 1
		return HttpResponse(json.dumps(response_data), content_type = 'application/json')
	else:
		if follower.id == followee.id:
			response_data['error'] = 'You Cannot follow yourself'
		else:
			response_data['error'] = 'You already following this User'
		return HttpResponse(json.dumps(response_data), content_type = 'application/json')	
			
@require_GET
@login_required
def unfollow(request, id):
	followee = get_object_or_404(MyUser, id = id)
	follower = request.user
	response_data = {'result': 0}
	if followee.id != follower.id and followee in follower.following.all():
		follower.following.remove(followee)
		response_data['result'] = 1
		return HttpResponse(json.dumps(response_data), content_type = 'application/json')
	else:
		if follower.id == followee.id:
			response_data['error'] = 'You Cannot unfollow yourself'
		else:
			response_data['error'] = 'You are not following this User'
		return HttpResponse(json.dumps(response_data), content_type = 'application/json')	



		

