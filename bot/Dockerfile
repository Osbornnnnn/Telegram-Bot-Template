FROM python:3.10-slim-buster AS builder

RUN mkdir -p /opt/Telegram-Bot/bot/src

WORKDIR /opt/Telegram-Bot/bot

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --upgrade setuptools \
  && pip install -r requirements.txt

COPY src /opt/Telegram-Bot/bot/src

CMD python -m src
