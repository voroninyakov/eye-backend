# Pet-learn project: Eye


АPI хостинга видео, для написания фронтенда к нему

## Предварительная настройка:

1. В папке `eye/ssl` замените в файлах ключ и сертификат на реальные, выпущенные вами.
2. Замените в `eye/settings/base.py` ключ django на строку хэша.
3. Проверьте, что репозиторий не повредился при установке.

## Запуск:

1. Сборка контейнера из `Dockerfile`
```commandline
docker build .
```

2. Сборка "compose" из `docker-compose.yml`
```commandline
docker compose up
```

3. Не забудьте запустить миграции для базы данных и выполнить их:

    - Миграция django auth:
        ```commandline
        docker compose exec web python /code/eye/manage.py migrate
        ```
    - Создание новых миграций:
      ```commandline
      docker compose exec web python /code/eye/manage.py makemigrations
      ```
    - Окончательная миграция:
      ```commandline
      docker compose exec web python /code/eye/manage.py migrate
      ```
4. А также создайте суперпользователя для админки:
    ```commandline
    docker compose exec web python /code/eye/manage.py createsuperuser
    ```
Всё готово, API будет доступно по локальному хосту 8000-го порта

## Технологии:

Со списком python-библиотек можно ознакомиться в `requirements.txt`, файл wait-for-it.sh взят из [репозитория vishnubob](https://github.com/vishnubob/wait-for-it)

### Документации:

- Python: https://www.python.org/
- DRF:        https://www.django-rest-framework.org/
- Django:     https://docs.djangoproject.com/
- Docker:     https://docs.docker.com/
- PostgreSQL: https://www.postgresql.org/
- Nginx:      https://nginx.org/en/docs/
- Uwsgi:      https://uwsgi-docs.readthedocs.io/en/latest/


