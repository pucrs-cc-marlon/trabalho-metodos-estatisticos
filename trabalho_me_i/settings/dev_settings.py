from trabalho_me_i.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ['172.18.0.3', '127.0.0.1']

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INSTALLED_APPS += (
    'debug_toolbar',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = []

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
