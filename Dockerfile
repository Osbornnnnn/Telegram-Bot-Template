FROM python:3.10-slim-buster AS builder

RUN mkdir /opt/shop-bot

RUN apt-get update \
    && apt-get -yy install libmariadb-dev \
    && apt-get -yy install gcc

WORKDIR /opt/shop-bot

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --upgrade setuptools \
  && pip install -r requirements.txt

COPY app /opt/shop-bot/app

CMD python -m app
