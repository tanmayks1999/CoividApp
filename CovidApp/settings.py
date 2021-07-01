"""
Django settings for CovidApp project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j8$w07(^jzz!#ytp=5l_2xapv8qxj_0!n@mz491fs#l(&jf=)b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    
ON_UPDATE_HANDLED_BY_DB = True

ALLOWED_HOSTS = ['*']

'''if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
'''

# FCM_DJANGO_SETTINGS = {
#     "FCM_SERVER_KEY" : "AAAALtPYOhs:APA91bHngAF5hIK31GQgDF9dEr4Ahttg2Lnuxi8fRhfRSMBaO1oB1WlcEdjVbTvPBX11IKwrddsy2CY6ioMEsZqiPSQAqos8RutmsBEsa2WUGhYcgajYKJU379_6xrKVvRnHVL1D3tYM"
# }

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'dailytracker.apps.DailytrackerConfig',
    'register.apps.RegisterConfig',
    'locations.apps.LocationsConfig',
    'django_email_verification',
    'phone_field',
    'channels',
    'fcm_django',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CovidApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CovidApp.wsgi.application'

ASGI_APPLICATION = "CovidApp.routing.application"

AUTH_USER_MODEL = 'register.Account'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : 'mydb',
        'USER'      : 'postgres',
        'PASSWORD'  : '1234',
        'HOST'      : 'localhost',
        'PORT'      : '5432',
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": ['redis://127.0.0.1:6379/1',]
        },
    },
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/home"

LOGOUT_REDIRECT_URL ="/login"


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'healthtracker1234@gmail.com' 
# EMAIL_HOST_PASSWORD = 'Pass@123'
EMAIL_HOST_PASSWORD = 'liuufxpntzhahvfq'
# EMAIL_HOST_USER = 'virani.pakshal@gmail.com' 
# EMAIL_HOST_PASSWORD = 'pakshal2498'
EMAIL_USE_TLS = True


'''EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_ADDRESS = 'virani.pakshal@gmail.com'
EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
EMAIL_PASSWORD = 'pakshal2498'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'mail_body.html'
EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
'''

import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


import django_heroku
django_heroku.settings(locals())
