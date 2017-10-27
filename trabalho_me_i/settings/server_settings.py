import dj_database_url
from trabalho_me_i.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = '/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
