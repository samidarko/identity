# syntax=docker/dockerfile:experimental
# local only
FROM python:3.9.4-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update
RUN apt-get install -y build-essential \
            iputils-ping \
            telnet

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
