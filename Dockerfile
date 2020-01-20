
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir code

WORKDIR /code

COPY ./Veacon /code
COPY ./requirements.txt /code

RUN pip install --no-cache-dir -r requirements.txt && python manage.py collectstatic --no-input
