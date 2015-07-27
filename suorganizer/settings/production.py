# https://docs.djangoproject.com/en/1.8/topics/settings/
# https://docs.djangoproject.com/en/1.8/ref/settings/

import os

import dj_database_url

from .base import *

# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{}'.format(
            os.path.abspath(
                os.path.join(
                    BASE_DIR, 'db.sqlite3'))),
    ),
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

EMAIL_HOST = os.environ.get('POSTMARK_SMTP_SERVER')
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('POSTMARK_API_TOKEN')
EMAIL_HOST_PASSWORD = os.environ.get('POSTMARK_API_TOKEN')
EMAIL_USE_TLS = True

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]


def get_cache():
    try:
        os.environ['MEMCACHE_SERVERS'] = (
            os.environ['MEMCACHIER_SERVERS'].replace(',', ';'))
        os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
        return {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'TIMEOUT': 500,
                'BINARY': True,
                'OPTIONS': {'tcp_nodelay': True},
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
            }
        }

CACHES = get_cache()
