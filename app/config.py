import pytz
from envparse import env


TIMEZONE = env.str("TZ", default=pytz.timezone("Europe/Moscow"))
TELEGRAM_TOKEN = env.str("SHOP_BOT_TG_TOKEN", default="")
DATABASE_URI = env.str("SHOP_BOT_DATABASE_URI", default="mariadb+mariadbconnector://root:root@127.0.0.1/shop_bot")
