"""
Django settings for zvook_test_task project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6o4ip1$j7c5it4#wk!s232ooz_tgna)7708g)&x$!azxtfbrpt'

# SECURITY WARNING: don't run with debug turned on in production!

INSTALLED_APPS = [
    'service.apps.ServiceConfig'
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'zvook_test_task.urls'

WSGI_APPLICATION = 'zvook_test_task.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOG_DIR = '/var/log/zvook'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)-8s] [%(message)s] '
                      '[%(name)s:%(lineno)s - %(funcName)s()]'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'logs.log'),
            'formatter': 'default'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }, 'celery': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    }
}

REDIS_IN_PROGRESS_SET_NAME = "in_progress"

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
