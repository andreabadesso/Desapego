"""
Django settings for Desapego_SV project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')tomad(q=!$tdvk+@z86z^w0obv81rhb+*zy-36a@o($1p9$od'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'Usuarios',
    'Hashtags',
    'Status',
    'Desapegos',
    'Comentarios',
    'rest_framework', 
    'Amigos',
    'djcelery',
    'Site',
)

#BROKER_URL = 'django://'

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates/"),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Desapego_SV.urls'

WSGI_APPLICATION = 'Desapego_SV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
"""
DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'desapego_db',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': 'desapego_admin',
		'PASSWORD': '@Badesso4712',
		'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
        }
}
"""
DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': '',
		'PASSWORD': '',
		'HOST': '',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
        }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

