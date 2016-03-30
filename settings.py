"""
Django settings for braintreeDemoApp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os, django
import socket
host_name = socket.gethostname()
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.dirname(__file__)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = '2u8hqr5qpp$qxm%kff!58c2-a*godh5o75ahyte*q=*gu8)d_#'


DEBUG = True



TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'billing',
    'registration'
)

OUR_APPS = (
    'home',
)

INSTALLED_APPS+=OUR_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '.g@.com'
EMAIL_HOST_PASSWORD = '@'
EMAIL_USE_TLS = True

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

LOGIN_REDIRECT_URL = '/home/'
ACCOUNT_ACTIVATION_DAYS = 7
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

REGISTRATION_OPEN = False



if host_name=="gaurav-All-Series" or host_name == "wagh":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': BASE_DIR+'/db.sqlite3',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }
else:
    DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "gateways",
        "USER": "dbuser",
        "PASSWORD": "1188",
        "HOST": "localhost",
        "PORT": "",

     }
    }



#braintree info Gauravwagh11
BRAINTREE_MERCHANT_ID =""
BRAINTREE_PUBLIC_KEY = ""
BRAINTREE_PRIVATE_KEY = ""

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'templates/media/')

print MEDIA_ROOT

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_URL = ''

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
   os.path.join(SITE_ROOT, 'templates/'),
)

