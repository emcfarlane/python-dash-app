# Based on:
# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
FROM python:3-slim AS build-env

ENV PYTHONUNBUFFERED True
ENV PYTHONIOENCODING utf-8

COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY . /app
WORKDIR /app

#FROM gcr.io/distroless/python3
FROM python:3-slim
COPY --from=build-env /root/.local /root/.local
COPY --from=build-env /app /app
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
