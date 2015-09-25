#coding=utf-8
"""
Django settings for lordrecommender project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '23is!a3mie53k=87ktvd0m1qcw=03pnkreh&uwq6x+($wa9v4('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DJANGO_SETTINGS_MODULE = "lordrecommender.settings"

# Application definition

INSTALLED_APPS = (
    # For django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
     
    # Third parties
    'django_extensions',
    'bootstrap3',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',   # for doc generation
    'rest_framework_gis',
    'djcelery',
    
    
    # My apps
    'devmng', # Developing management
    'business', # define the business entity as recommending target
    'recommendation', # core recommendation
    'users',  # users management
    'api', 
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'lordrecommender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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


WSGI_APPLICATION = 'lordrecommender.wsgi.application'
#CSRF_COOKIE_DOMAIN = None

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': 'lordrecommender_debug',
        'USER': 'postgres',
        'PASSWORD':'Hacker1218',
        'TEST': {
                    'charset': 'utf-8',
                     },
    },
    # 'geodjango':{
    #      'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #      'NAME': 'geodjango',
    #      'USER': 'postgres',
    #      'PASSWORD':'Hacker1218',
    # }
}



# Setting for geodjango (Perhaps not needed)
#GEOS_LIBRARY_PATH = 'D:/GEOLibs/OSGeo4W/share/gdal'
GDAL_LIBRARY_PATH = 'D:/GEOLibs/OSGeo4W/bin/gdal111.dll'

# Celery settings
import djcelery
djcelery.setup_loader()
REDIS_SERVER = '192.168.1.8:6379'
BROKER_URL = 'redis://%s/0' % REDIS_SERVER
CELERY_RESULT_BACKEND = 'redis://%s/0' % REDIS_SERVER
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' # 定时任务
# CELERY_ENABLE_UTC = False # 不是用UTC
# CELERY_TIMEZONE = 'Asia/Shanghai' 
# CELERY_TASK_RESULT_EXPIRES = 10 #任务结果的时效时间
# CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'] # 允许的格式


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATICFILES_DIRS = [
    'G:/Download/static',
    os.path.join(BASE_DIR, 'recommendation/static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Custom image url
IMAGE_URL = 'images/'
STATIC_IMAGE_ROOT = os.path.join(BASE_DIR, 'images/static/')


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'PAGINATE_BY': 10,
    # 'PAGINATE_BY_PARAM': 'page_size',
    # 'MAX_PAGINATE_BY': 100
}


CACHES = {
    # This uses local memory for development
    # 'debug': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake',
    #     'TIMEOUT': 60 * 30,
    #     'OPTIONS': {
    #         'MAX_ENTRIES': 1000
    #     }
    # },
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s/1" % REDIS_SERVER,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            #"IGNORE_EXCEPTIONS": True,
        }
    }
}
