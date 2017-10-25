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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER':  'postgres',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_e_cup',
        },
    },
}
