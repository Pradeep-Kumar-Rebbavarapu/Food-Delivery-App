import os

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

application = get_wsgi_application()
call_command("gunicorn", "server.wsgi:application")
