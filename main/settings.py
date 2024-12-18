from pathlib import Path
from decouple import config
from datetime import timedelta
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-f8+gz#734=f$lp!at*kmyrl=09745t=i!odfo67y4*7@*vbb=w"
# SECRET_KEY = config("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'corsheaders',
 'rest_framework',
 'rest_framework.authtoken',
 'users',
 'blog',
 'rest_framework_simplejwt',
]

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 'corsheaders.middleware.CorsMiddleware',
 'django.middleware.common.CommonMiddleware',
 "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
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

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
 'http://localhost:3000',
 'https://vercel.app',
 'https://blog-app-eosin-nine.vercel.app'
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
 'DEFAULT_AUTHENTICATION_CLASSES': [
  'rest_framework_simplejwt.authentication.JWTAuthentication',
 ],
 'DEFAULT_PARSER_CLASSES': [
  'rest_framework.parsers.JSONParser',
  'rest_framework.parsers.MultiPartParser',
 ],
}

AUTHENTICATION_BACKENDS = {
 "django.contrib.auth.backends.ModelBackend"
}

SIMPLE_JWT = {
 'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = []

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')