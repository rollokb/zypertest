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
