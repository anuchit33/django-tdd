DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_web',
        'USER': 'admin',
        'PASSWORD' : '112233',
        'HOST' : 'db_web',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '../static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '../media/'