# Celery test
</hr>


Utworzenie obrazu z RabbitMQ i Redis `docker-compose`:
```bash
docker-compose up -d
```

Uruchomienie:
```
$ docker ps
```

## Użycie
Uruchomienie Celery:
```bash
$ celery -A tasks worker -l info 
```



```python
$ python
>>> import tasks
>>> t = tasks.long_runnning_oper.delay("Hello world!")
>>> result = tasks.long_runnning_oper.AsyncResult(t.task_id)
>>> result.get()
```

