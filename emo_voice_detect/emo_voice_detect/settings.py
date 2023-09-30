"""
Django settings for emo_voice_detect project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$^4o5t$-^9h5l)#@szz6%@^j*c6zwosh3kgtryv%&!#!)_t4jj'

# emotion_detection/settings.py

# Google Cloud Vision API settings
GOOGLE_CLOUD_VISION_API_KEY = 'MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCU4mbzkKeawsAN\nuSlfVRnW9Fk5CHuHU5DB3qqXKMjoAYipyOcViSIzySse6sn73Sk9duzBMKV6tk2r\n5wKQXWmHiKwJITbgBsVNc3JQPzWWSnoHaB4yWcBdsUeR4kCRTg1gYeQO8zk6GplQ\nyyzP13kqVi80U+3agqI3zhffwA1toRG//9ynGHjlolKx4mqJVuSY4t56Q5EIFai9\n6nVed8hEjYWcCFUGvGWRXCcGE4L7Ft7VFQRCR+jjlfe9i/c7uc7V+JkVMxerVUOe\nor5povX9OkJ53eLQoQMK7WBsB4RCMk8CmQnW7Sdja7MeLcirzJ+WXkeHHYlyHBfX\naSUai/lhAgMBAAECggEAElKoq+oODnhQTYAPrOlaxD8PKfs2xKlOo+Vk5jSBQThL\nGuYcNmTJnkjwMx5fHE2UETntGjuD6g28kl7cTGsKnUD/NyJsz/ZVWtpN471buXLS\nAM5aBQVRrNYwAi6vlpJeCBIUEJjzXoi+fJh8m9mfUkwIBC8eEynHkAmfm4xVuruL\nV3aYy85YHvxX6sF0Az4wqP2kd4+b+8dE6YEUsVO22D7bW61LBqpkQYT7kVXPWfDN\nin7WTE7McHSSXCgxLCBgndtDud01FrmQuX+HJDf4E3b1C5FF9gkarIgfncg4sc2x\nZfZaV/RgBDEzfqacEF3puRHydhITjjc8+q2RvF5ipwKBgQDDQYeLVHa7yeLDJwkL\nSwMxNZFjz54nE/ejW8M/LSOo2dN2TMLSCeDTrKPnHdQ4IRoQyZwgmtO/ZdjT33SA\nE9BCSqV1AVFVAcMhTCOt94DsA1coyEUMoxFtSCpEzWit7cRHOyGoh+WEBhitjvi9\nvAA3gziqaAOwUuSYE2lup9rZrwKBgQDDM8WEbW6PYFLu5wbMrV0FAIBslViZ8r6S\nifispldvIi2ncGM2x+8DYhHdeJLPhG1XDratkHiIzHhJJ6njWQ9wYiE+KfmhZqBC\nkXXzTPImTmj2y3BySDBTg8vQ29YhF8cqh5jjUoe58g04IEm6//yV0BcrxuTans2D\nOls00sPx7wKBgF2Q0FAvGHqiotybnxTfTFdPcS1gN0xIoDmS5nwmuFjYkSG2ZQFb\npHYq25wLyj9fdWsoAX4KU3/7YS0efmhFll2+AY2RJRVUM9qH7u0Vlp0CeMjdN2F3\n3wj8NO0ldY0rTAxKRLXK8WwTs82vnnjlV0FCy2u1Tlc3Ub2iR7q0CwaXAoGAFiLg\n20utpgS+YulAFCX0zoRoC+hDy/GDOwr6cFnMwIWXt80+8w9pQ3DzpbHutCnIXH8G\nqFgh0yGc4m7lDSskXRJDwtDvxiXlNqdYQOcQ7tclgBdCATO+hzoC+wRzG/2eUGxg\nIidRzPxuE1dWBSbSdgrLFePQQBqSI7eScEMWhXECgYBY69SPPtlLBzXvhBB/32AE\nJuhjIpooMFcg6SWz2GwWeYfiYmrymKFBSfqYo76w9NZdh0mbxo4LW0NmCRjQyk4e\nxHhTaUOLc4QRdyqv2WDYrCDxpDwy7jhoY0Q4GWeZ/7WV3v/a1myOoycAu15/2uyF\nGfMupmHFA6C3hUAObohSaw=='  # Path to your API key JSON file

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myApp"
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

ROOT_URLCONF = 'emo_voice_detect.urls'

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

WSGI_APPLICATION = 'emo_voice_detect.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = ''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
