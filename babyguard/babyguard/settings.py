"""
Django settings for babyguard project.

Generated by 'django-admin startproject' using Django 1.8.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import os
BASE_DIR = os.path.dirname(__file__)

import sys 
sys.path.extend([
    '/data/util/CoreFunction/',
    '/data/util',
    '/data/',
    '/home/daiqiang/gif_search_data/util/CoreFunction',
    '/home/daiqiang/gif_search_data/tags_index_for_gif',
    '/Users/xinmei365/gif_search_data/util/CoreFunction',
    '/Users/xinmei365/gif_search_data/tags_index_for_gif',
     ])  
import pyUsage
print (pyUsage.get_cur_info(), 'BASE_DIR= ', BASE_DIR)
import pyIO
import pyString

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h)44u3bdct=gm-k684$o(0j4i1e5@d=h=qmd$p(u5l)k^-ai*d'

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
    'debug_toolbar',
    'babyguard.account',
    'babyguard.ask',
    'babyguard.audio',
    'babyguard.check',
    'babyguard.course',
    'babyguard.food',
    'babyguard.sns',
    'babyguard.video',
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

ROOT_URLCONF = 'babyguard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/babyguard/account/templates',
            BASE_DIR + '/babyguard/ask/templates',
            BASE_DIR + '/babyguard/audio/templates',
            BASE_DIR + '/babyguard/auth/templates',
			BASE_DIR + '/babyguard/check/templates',
			BASE_DIR + '/babyguard/chart/templates',
			BASE_DIR + '/babyguard/course/templates',
			BASE_DIR + '/babyguard/food/templates',
			BASE_DIR + '/babyguard/sns/templates',
			BASE_DIR + '/babyguard/video/templates',
			BASE_DIR + '/babyguard/lab/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'babyguard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'
USE_TZ = True
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'Asia/Shanghai'
USER_TZ = False
FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= BASE_DIR + '/babyguard/'
STATICFILES_DIRS = (
    BASE_DIR + '/babyguard/' + STATIC_URL,
)
print ('STATICFILES_DIRS= ', STATICFILES_DIRS )
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
    )
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

INTERNAL_IPS = ('127.0.0.1','::1','61.135.172.68','10.97.32.188','1.15.113.109','61.135.172.68',)

import redisco
#redisco.connection_setup(host='123.206.69.25', port=6379, db=0)
redisco.connection_setup(host='172.31.28.109', port=7000, db=0)
#redisco.connection_setup(host='localhost', port=22121, db=0)
#res = redisco.connection_setup(host='localhost', port=7001, db=0)
#print (pyUsage.get_cur_info(), 'res= ', res)
#from rediscluster import StrictRedisCluster
#startup_nodes = [{"host": "127.0.0.1", "port": "19000"}]
#rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)



