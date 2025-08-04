from celery import shared_task


@shared_task
def add(x, y):
    print(x+y)
    return x + y

@shared_task
def answer():
    print("I love python")
    return"I love python"