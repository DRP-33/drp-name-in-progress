FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp/backend

COPY CI/requirements.txt /webapp/
COPY website /webapp/backend

RUN pip install -r ../requirements.txt

CMD ["gunicorn", "backend.website.wsgi"]