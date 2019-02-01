import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
DEBUG = (os.environ.get('DEBUG', '').lower() == 'true')
# Application definition


# Django is typically set up for user facing websites,
# most of the contrib applications are unnessary for APIs.
# Applications like auth are focused on users, an admin
# isn't nessary.
INSTALLED_APPS = [
    'zyper.images'
]


ROOT_URLCONF = 'zyper.urls'
WSGI_APPLICATION = 'zyper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# APIs should use UTC and leave display of times up to clients
TIME_ZONE = 'UTC'
USE_TZ = True


# File storage in production wouldn't be done via envars, but an
# AWS policy between the process and bucket.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_STORAGE_BUCKET_NAME = 'zypertest'
AWS_QUERYSTRING_AUTH = False


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 100,
    # At this point I don't know how this API auths.
    # Perhaps there isn't any. So dissabling
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    ),
}

CELERY_BROKER_URL = 'amqp://localhost'
