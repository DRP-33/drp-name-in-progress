FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

COPY CI/requirements.txt /webapp/
COPY website /webapp/backend

RUN pip install -r requirements.txt