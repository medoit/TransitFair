import os
import sys
from pathlib import Path

# Получаем путь к базовой директории
BASE_DIR = Path(__file__).resolve().parent.parent

# Добавляем папку apps в путь, чтобы Django видел приложения в папке apps
sys.path.append(os.path.join(BASE_DIR, "apps"))

# Разделяем секретные ключи и настройки для безопасности
SECRET_KEY = 'django-insecure-(*xr&0-^*p@(twm&z54#-^vx4xb4yk(vj*r3drm!^4jn)d=ye^'

# Дебаг-режим (не включать в продакшн!)
DEBUG = True

# Список хостов, которым разрешено подключаться
ALLOWED_HOSTS = []

# Приложения, которые включены в проект
INSTALLED_APPS = [
    # Стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # другие приложения
    'apps.transactions',
    'apps.benefits',
    'apps.citizens',
    'apps.сitizen_сards',
]

# Миддлвары
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основные маршруты (для статичных страниц и админки)
ROOT_URLCONF = 'TransitFair.urls'

# Шаблоны
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

# Конфигурация WSGI (для развертывания)
WSGI_APPLICATION = 'TransitFair.wsgi.application'

# База данных (по умолчанию — SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Секреты (для продакшн-окружения лучше использовать переменные окружения или конфигурационные файлы)
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

# Локализация и языковые настройки
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS, изображения)
STATIC_URL = '/static/'

# Разрешения для статики (если нужно, можно добавить обработку на продакшн)
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Временные файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'