import os 

from pathlib import Path

import environs as environs
from dotenv import load_dotenv

load_dotenv()

env = environs.Env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

INTERNAL_IPS = [
    os.environ.get("INTERNAL_IPS")
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'debug_toolbar',
    'django_filters',
    
    'core',
    'ecommerce_api',
    'cart',
    'coupon_api',
    'orders',
    'ecommerce_celery',
    'payment',
    'mailing',
    'cdek',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


if env.bool("SWITCH_DB"):
    DATABASES = {
        'default': {
            "ENGINE": os.environ.get("SQL_ENGINE_TEST"),
            "NAME": os.environ.get("SQL_DATABASE_TEST"),
        }
    }

else:
    DATABASES = {
        'default': {
            "ENGINE": os.environ.get("SQL_ENGINE"),
            "NAME": os.environ.get("SQL_DATABASE"),
            "USER": os.environ.get("SQL_USER"),
            "PASSWORD": os.environ.get("SQL_PASSWORD"),
            "HOST": os.environ.get("SQL_HOST"),
            "PORT": os.environ.get("SQL_PORT"),
        }
    }


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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True 


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'UPLOADED_FILES_USE_URL': False,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}


CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") 
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = [os.environ.get("CELERY_ACCEPT_CONTENT")]  
CELERY_RESULT_SERIALIZER = os.environ.get("CELERY_RESULT_SERIALIZER")

EMAIL_BACKEND =os.environ.get("EMAIL_BACKEND")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
