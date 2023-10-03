FROM python:3.11.1-slim-buster
LABEL maintainer="megah1t"

ENV PYTHONUNBUFFERED 1

# Установка Chromium и Chromedriver
RUN apt-get update && apt-get install -y chromium chromium-driver

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chown -R 755 /vol/web/
RUN chmod -R 777 /vol/web/media/

# Запустить контейнер от имени суперпользователя
USER root
