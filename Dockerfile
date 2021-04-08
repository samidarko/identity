# syntax=docker/dockerfile:experimental
# local only
FROM python:3.9.4-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /code

COPY ./callbacks.py ./callbacks.py
COPY ./main.py ./main.py
COPY ./models.py ./models.py
COPY ./requirements.txt ./requirements.txt

RUN apt-get update
RUN apt-get install -y build-essential \
            iputils-ping \
            telnet

RUN pip install -r requirements.txt


ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "main:app" ]
