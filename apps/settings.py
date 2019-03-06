"""
Django settings for CLEO project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '46yqb-l-qig_r1olx$j@hxa45phmx@3q*v6@pz($d%yj#jw2x2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modules.Main',
    'modules.Empleado',
    'modules.Sala',
    'modules.Maquina',
    'modules.Tratamiento',
    'modules.Producto',
    'modules.Promocion',
    'modules.Publicidad',
    'modules.Cliente',
    'modules.Notificacion'
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

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

                os.path.join(BASE_DIR, '/modules/Main/templates'),
                os.path.join(BASE_DIR, '/modules/Empleado/templates'),
                os.path.join(BASE_DIR, '/modules/Sala/templates'),
                os.path.join(BASE_DIR, '/modules/Maquina/templates'),
                os.path.join(BASE_DIR, '/modules/Tratamiento/templates'),
                os.path.join(BASE_DIR, '/modules/Producto/templates'),
                os.path.join(BASE_DIR, '/modules/Promocion/templates'),
                os.path.join(BASE_DIR, '/modules/Publicidad/templates'),
                os.path.join(BASE_DIR, '/modules/Cliente/templates'),
                os.path.join(BASE_DIR, '/modules/Notificacion/templates'),

        ],
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

WSGI_APPLICATION = 'apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'CLEO',
        'USER': 'root',
        'PASSWORD': 'root2018',
        'HOST': 'localhost', #'db',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',

    'OPTIONS': {'sql_mode': 'TRADITIONAL', 'use_pure': True, 'use_unicode': True, 'charset': 'utf8mb4',
            'collation': 'utf8mb4_general_ci','get_warnings':False},
    }

}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-es'

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cleo.tfg2019@gmail.com'
EMAIL_HOST_PASSWORD = 'cleo2019'
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
