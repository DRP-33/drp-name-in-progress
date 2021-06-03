FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp/backend

COPY CI/requirements.txt /webapp/
COPY backend /webapp/backend

RUN pip install -r ../requirements.txt

CMD ["gunicorn", "website.wsgi"]