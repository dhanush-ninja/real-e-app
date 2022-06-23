from __future__ import absolute_import

import os

from celery import Celery
from realestate.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{realestate}}.settings.development")

app = Celery("realestate")

app.config_from_object("realestate.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)