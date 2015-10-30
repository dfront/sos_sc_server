"""
Django settings for helpsystem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys
import site

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '38qx=jf8xv#xx%n&7dpl67f$xf0)vd88t_2+gkft!m$bzasu6j'

DEBUG = True


TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.sos_server.us']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'staticflatpages.middleware.StaticFlatpageFallbackMiddleware'
)



TEMPLATE_CONTEXT_PROCESSORS = (

    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    #'main.custom_context_processors.template_base_var',
    #'pessoa.custom_context_processors.template_base_var',
    'django.core.context_processors.request',

    #'social_auth.context_processors.social_auth_by_name_backends',
    #'social_auth.context_processors.social_auth_backends',
    #'social_auth.context_processors.social_auth_by_type_backends',
    #'social_auth.context_processors.social_auth_login_redirect',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH,'static/templates/'),
    os.path.join(PROJECT_ROOT_PATH,'static/admin/'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',  
    'django.contrib.flatpages',
     'crispy_forms',
    'abrigo'   
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'sos_server.wsgi.application'

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql', 
	'NAME': 'sos',  
	'USER': 'sos',   
	'PASSWORD': 'sos123',       
	'HOST': 'localhost',                
	'PORT': '3306',    
     }
}

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, "/static/")

STATIC_URL = '/static/'

SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH,"static/media/")

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = "/contas/login/"

USER_HOME_URL = "/contas/home"

ACCOUNT_ACTIVATION_DAYS=7

AUTH_PROFILE_MODULE = 'pessoa.Pessoa'

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

OPENFIRE_HOST  = 'openfire.us'
OPENFIRE_KEY   = "XaoUU9Y6AzOa7T75"
EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = ''

EMAIL_PORT = 587

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format'  : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/projetos/sos_server/site.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'ERROR',
        },
        'agenda': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
       'pessoa': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'municipios': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'main': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'pagina_dinamica': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    }
}
