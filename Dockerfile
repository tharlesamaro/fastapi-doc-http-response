FROM python:3.11.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && pip install --upgrade pip

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD sh -c "while true; do sleep 3600; done"