from celery import Celery
import time

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def long_runnning_oper(message: str):
    time.sleep(30)
    return f"Delayed message: {message}"
