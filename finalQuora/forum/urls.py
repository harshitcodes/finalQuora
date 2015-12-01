from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^question_form/', 'forum.views.question_form', name = 'question_form'),
     url(r'^answer_form/', 'forum.views.answer_form', name = 'answer_form'),
) 

