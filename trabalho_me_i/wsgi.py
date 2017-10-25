"""
WSGI config for trabalho_me_i project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

if os.environ.get('AMBIENTE') == 'dev':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trabalho_me_i.settings.dev_settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trabalho_me_i.settings.server_settings")

application = get_wsgi_application()
