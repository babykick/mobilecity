#coding=utf-8
from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lordrecommender.settings')

from django.conf import settings

app = Celery('lordrecommender')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#For the database backend you must use:
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)

#For the cache backend you can use:
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend',
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))