import os, sys
sys.path.append('/var/projetos/sos_server/')
os.environ['DJANGO_SETTINGS_MODULE']='settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/projetos/.python-eggs/'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
