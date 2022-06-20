from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
DOMAIN = env("DOMAIN")
SITE_NAME = env("SITE_NAME")

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRESQL_ENGINE"),
        "NAME": env("POSTGRESQL_NAME"),
        "USER": env("POSTGRESQL_DB_USER"),
        "PASSWORD": env("POSTGRESQL_PASSWORD"),
        "HOST": env("POSTGRESQL_HOST"),
        "PORT": env("POSTGRESQL_PORT"),
    }
}
