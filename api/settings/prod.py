"""Production Settings."""
import os
import dj_database_url
from .dev import *  # noqa: F403, F401


# cSpell:ignore boto Boto

############
# DATABASE #
############
DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}

############
# SECURITY #
############

DEBUG = bool(os.getenv("DJANGO_DEBUG", ""))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']