import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'trprweb.trprweb.settings'
application = WSGIHandler()
