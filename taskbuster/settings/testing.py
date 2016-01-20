# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DATABASE SETTINGS: Use PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

# TEST FIXTURE SETTINGS
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)