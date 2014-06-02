"""
Django settings for PreguntMatic project.

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
SECRET_KEY = '$l34j3rwc8f7l80y06s*h1a89oo=cn%@r!e=%!n-m&r56^)w1i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*',]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    
)


# Application definition

INSTALLED_APPS = (
    #'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Usuaris',
    'Preguntes',
    'eines',
    'dajaxice',
    'dajax',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PreguntMatic.urls'

WSGI_APPLICATION = 'PreguntMatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#Base de dades
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            'NAME':'preguntmatic',
    'USER':'preguntmatic',
'PASSWORD': 'ies',
'HOST':'localhost',
'PORT':'3306',
        
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ca'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Templates
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'TEMPLATES'),]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "fitxers_estatics"),
)

##Defineixo on van les imatges del titols
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#Login i logout
LOGIN_URL = '/usuaris/login'
LOGOUT_URL = '/usuaris/logout'
