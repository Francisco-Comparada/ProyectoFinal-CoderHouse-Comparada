"""
Django settings for Urbans_Sneakers project.

Generated by 'django-admin startproject' using Django 4.0.6.

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
SECRET_KEY = 'django-insecure-z1o(q=(rm!k_=ozidmos-whjm#emllmeq7#@xmb$@4-ayfea43'

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
    #apps
    'Productos',
    'users',
    'bootstrap5',
    'Cart',
    'Orders',
    'customize_page',
    'Contact',
    
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

ROOT_URLCONF = 'Urbans_Sneakers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # los context_processors los utilizamos para poder ver la informacion que necesitemos desde los templates 
                # fueron decladaros en sus respectivas apps 
                'Productos.context_processors.id_category',
                'Productos.context_processors.id_sub_category',
                'Productos.context_processors.id_product',
                'Cart.context_processors.total_cart_amount',
                'Cart.context_processors.total_product',
                'customize_page.context_processors.id_banner',
                'customize_page.context_processors.id_featured_products',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'Urbans_Sneakers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#base de datos PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'urbans_sneakers',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST' : '127.0.0.1',
        'DATABASE_PORT':'5432'
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

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'),)


#para poder ver las imagenes con url
MEDIA_ROOT= os.path.join (BASE_DIR,'media')
MEDIA_URL='media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'users/login/'
LOGOUT_REDIRECT_URL = "/"


# esto es para el mail se cambia contraseña cuando cada vez que subo a git 
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'urbanssneakers22@gmail.com'
EMAIL_HOST_PASSWORD = 'vsltfrsiyxdacyhu'
EMAIL_PORT = 587
