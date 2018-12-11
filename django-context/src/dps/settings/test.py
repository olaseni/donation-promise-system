# noinspection PyUnresolvedReferences
from .base import *  # noqa: F401

ENVIRONMENT = 'test'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# filter out cache
INSTALLED_APPS = [app for app in INSTALLED_APPS if not 'cache' in app]

# Redis
# https://redis.io/
REDIS_SERVER = {}

# Caches
# http://niwinz.github.io/django-redis/latest/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "OPTIONS": {
            "CLIENT_CLASS": "mockredis.client.mock_redis_client",
        }
    }
}

# cacheops
CACHEOPS_REDIS = {}
CACHEOPS_DEFAULTS = {}
CACHEOPS = {}
