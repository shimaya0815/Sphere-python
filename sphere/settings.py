import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Use environment variable to keep the secret key secure in production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-6+xuj^1wz75_!-pa2#s_9ffk%5#@)dhu_lu#dbj9cdons^x%_=')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') != 'False'

# Allow all host headers
ALLOWED_HOSTS = ['cb050d38fc4a494a9c2c68f408cc585d.vfs.cloud9.ap-northeast-1.amazonaws.com', 'sphere-application-9e82ba57c4f8.herokuapp.com', 'localhost']

CSRF_TRUSTED_ORIGINS = [
    'https://*.vfs.cloud9.ap-northeast-1.amazonaws.com',
    'https://*.herokuapp.com'
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.vfs.cloud9.ap-northeast-1.amazonaws.com',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'sphere.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sphere.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': 'todo',  # 新しく作成したデータベース名
    #    'USER': 'myuser',      # 新しく作成したユーザー名
    #    'PASSWORD': 'mypassword',  # ユーザーのパスワード
    #    'HOST': 'localhost',
    #    'PORT': '5432',
    #}
#}

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Password validation
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
LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'