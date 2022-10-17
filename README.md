# API YAMDB

API для получения информации и обсуждения наиболее интересных произведений

## Стэк технологий:

- Python
- Django Rest Framework
- Postgres
- Docker

### Документация и возможности API:

К проекту подключен redoc. Для просмотра документации используйте эндпойнт `redoc/`

### Начало:

- Склонируйте репозитрий на свой компьютер
- Создайте `.env` файл в директории `infra/`, в котором должны содержаться следующие переменные:

  > DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
  > DB_NAME= # имя базы данных\
  > POSTGRES_USER= # логин для подключения к базе данных\
  > POSTGRES_PASSWORD= # пароль для подключения к БД\
  > DB_HOST=db\ # название сервиса\
  > DB_PORT=5432\ # порт для подключения к БД

- Шаблон `.env` файла:

  > DB_ENGINE=django.db.backends.postgresql
  > DB_NAME=postgres
  > POSTGRES_USER=postgres
  > POSTGRES_PASSWORD=postgres
  > DB_HOST=db
  > DB_PORT=5432

- Из папки `infra/` соберите образ с запущенным Docker при помощи docker-compose
  `$ docker-compose up -d --build`
- Примените миграции
  `$ docker-compose exec web python manage.py migrate`
- Соберите статику
  `$ docker-compose exec web python manage.py collectstatic --no-input`
- Для доступа к админке не забудьте создать суперюзера
  `$ docker-compose exec web python manage.py createsuperuser`

Бэйдж:
[![yamdb_workflow](https://github.com/LightOfMidas/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/LightOfMidas/yamdb_final/actions/workflows/yamdb_workflow.yml)
