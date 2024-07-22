from celery import shared_task
from time import sleep

@shared_task
def sub(X,Y):
    sleep(10)
    return X-Y