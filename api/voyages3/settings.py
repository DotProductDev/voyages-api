"""
Django settings for voyages3 project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from .localsettings import *

from pathlib import Path

from django.core.files.storage import DefaultStorage
from filebrowser.sites import FileBrowserSite

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

TINYMCE_FILEBROWSER=True

INSTALLED_APPS = [
	'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
	'voyage',
    'assessment',
    'past',
    'common',
    'blog',
    'geo',
    'document',
	'contribute',
    'tinymce',
    'rest_framework',
    'rest_framework.authtoken',
    'captcha',
    'nested_admin'
]

#the below are defined in localsettings.
#i couldn't figure out how to make the .pg_pass file work in docker
#and it seemed that if i did, it might not translate to production deployment seamlessly anyways

#DRF settings
#via https://www.django-rest-framework.org/api-guide/metadata/#setting-the-metadata-scheme
REST_FRAMEWORK = {
	'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
	'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.TokenAuthentication'
    ]
}

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

CORS_ALLOW_ALL_ORIGINS=True

CORS_ALLOW_CREDENTIALS= True

ROOT_URLCONF = 'voyages3.urls'

CORS_EXPOSE_HEADERS = ["total_results_count"]

ALLOWED_HOSTS=['*']

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt-br',_('Portuguese'))
]




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

WSGI_APPLICATION = 'voyages3.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH=False

STATIC_ROOT='static'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'

# Default FileBrowser site
site = FileBrowserSite(name='filebrowser')

site.storage.location = "static"
site.directory="uploads/"
site.storage.base_url = "/static/abcdefg"

TINYMCE_JS_URL="tinymce/tinymce.min.js"
TINYMCE_DEFAULT_CONFIG = {
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
