import pytz
from envparse import env


# Способ получить часовой пояс из переменной среды. Если он не установлен, будет использоваться значение по умолчанию.
# Установите свой часовой пояс.
TIMEZONE = env.str("TZ", default=pytz.timezone("Europe/Moscow"))

# Способ получить токен телеграмма из переменной окружения. Если он не установлен, будет использоваться значение по умолчанию.
# Поле default оставьте пустым.
TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", default="")

# Способ получить URI базы данных из переменной среды. Если он не установлен, будет использоваться значение по умолчанию.
# Установите свои данные
DATABASE_URI = env.str("DATABASE_URI", default="mariadb+mariadbconnector://DB_USERNAME:DB_PASSWORD@DB_HOST/DB_NAME")
