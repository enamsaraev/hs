import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_celery.settings")

app = Celery("ecommerce_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()