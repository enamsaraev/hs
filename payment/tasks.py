from __future__ import absolute_import, unicode_literals
from ecommerce_celery.celery import app


@app.task
def add(x, y):
    print(x+y)