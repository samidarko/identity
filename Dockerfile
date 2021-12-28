# syntax=docker/dockerfile:experimental
# local only
FROM python:3.9.4-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update \
  && apt-get install -y build-essential

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0"]
CMD ["--port", "8000"]
