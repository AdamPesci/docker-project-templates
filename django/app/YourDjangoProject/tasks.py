from celery import shared_task


@shared_task
def debug_task():
    return "Hello World!"


@shared_task()
def add(x, y):
    return x + y


@shared_task()
def sub(x, y):
    return x - y
