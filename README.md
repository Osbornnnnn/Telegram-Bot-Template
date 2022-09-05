# Telegram-Bot-Template
Шаблон для быстрого написания Telegram бота с использованием Docker.

# Конфигурация
Это приложение имеет несколько обязательных переменных среды для запуска (см. [bot/src/config.py](https://github.com/Osbornnnnn/Telegram-Bot-Template/blob/main/bot/src/config.py))

`TELEGRAM_TOKEN` - токен Телеграм бота от BotFather. [Документация для Телеграм ботов](https://core.telegram.org/bots)

`DATABASE_URI` - ссылка для подключения к БД PostgreSQL.

Вы можете использовать другую базу данных, для этого необходимо в файле [requirements.txt](https://github.com/Osbornnnnn/Telegram-Bot-Template/blob/main/bot/requirements.txt) изменить 7 строку `psycopg2-binary` на connector для вашей базы данных.

# Запуск приложения

## Зависимости
* Docker
* PostgreSQL

## Запуск приложения локально
1. Установите все необходимые зависимости:

    ```bash
    pip install -r bot/requirements.txt
    ```
2. Измените конфигурацию в [`bot/src/config.py`](https://github.com/Osbornnnnn/Telegram-Bot-Template/blob/main/bot/src/config.py)
3. Запустите приложение:

    ```bash
    python -m bot/src
    ```

## Запуск с использованием Docker

Чтобы запустить это приложение с помощью **docker**, используем **docker-compose**:
1. Переименовываем файл [**.env-example**](https://github.com/Osbornnnnn/Telegram-Bot-Template/blob/main/.env-example) в **.env**
2. Меняем переменные на свои.
3. В консоли пишем:

    ```bash
    docker-compose up -d
    ``` 
