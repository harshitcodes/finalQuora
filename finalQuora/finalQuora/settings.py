"""
Django settings for finalQuora project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTH_USER_MODEL = "user.MyUser"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')si4d&_b!ch&hczr$mt0_s-m92r9mupv9x7f%2++p&!tx#761('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forum',
    'user',
    'materializeform',
    'material',
    # 'social.apps.django_app.default',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'finalQuora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                
                
            ],
        },
    },
]

WSGI_APPLICATION = 'finalQuora.wsgi.application'

# AUTHENTICATION_BACKENDS = (
# 	# 'social.backends.twitter.TwitterBackend',
# 	'social.backends.facebook.FacebookBackend',
# 	'social.backends.google.GoogleOAuthBackend',
# 	'django.contrib.auth.backends.ModelBackend',
# )

# # Database
# # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# SOCIAL_AUTH_GOOGLE_OAUTH_KEY = '742127075100-iboc2e0tfu6ft3kv210uvuarfapuog12.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH_SECRET = 'P1XiPbspJ3l080YKpEX7K0SR'

# FACEBOOK_APP_ID='1508132399486085'
# FACEBOOK_API_SECRET='79a12d0d089ca551a081a34dbaa7dbeb'


DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'finalQuora',
	       'PASSWORD': 'StrongPassword',
	    'USER': 'root',
	    'HOST': '127.0.0.1',
	    'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'harshit.bvcoe'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
