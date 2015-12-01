from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login_form/', 'user.views.login_form', name = 'login_form'),
    url(r'^hello$', 'user.views.hello', name = 'hello'),
    url(r'^logout/$','user.views.logoutview', name='logout'),   
    url(r'^signup_form/', 'user.views.signup_form', name = 'signup_form'),
    url(r'^base$', 'user.views.base', name = 'base'),
    url(r'(?P<id>[0-9]+)/write_answer/$', 'user.views.write_answer', name ='write_answer'),
    url(r'(?P<id>\d+)/follow/$', 'user.views.follow', name ='follow'),
    url(r'(?P<id>\d+)/unfollow/$', 'user.views.unfollow', name ='unfollow'),
    url(r'^otherhome/$', 'user.views.otherhome', name = 'otherhome'),
    url(r'^$', 'user.views.base', name = 'base'),
    url(r'^home/$', 'user.views.home', name='home'),
    url(r'^activate/$', 'user.views.activateaccount', name='activate'),
    url(r'^success/$', 'user.views.success', name='success'),
    url(r'^password_reset_request/$', 'user.views.password_reset_request', name='password_reset_request'),
    url(r'^reset/$', 'user.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'user.views.reset_confirm', name='password_reset_confirm'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    #url(r'^postsignup/$', 'user.views.postsignup', name = 'postsignup')
) 