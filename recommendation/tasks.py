from __future__ import absolute_import
from .models import Comment
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

 