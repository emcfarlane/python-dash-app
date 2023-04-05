# Based on:
# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
FROM python:3-slim AS build-env

ENV PYTHONUNBUFFERED True
ENV PYTHONIOENCODING utf-8

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
