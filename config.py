

from os import getenv, path

# ------------------
class Configuration: # pylint: disable=too-few-public-methods
    """ configuration class """
    
# ---- important ----
    # api id of your telegram account (required)
    API_ID = getenv("API_ID")
    # api hash of your telegram account (required)
    API_HASH = getenv("API_HASH")
    # create a session using command [ python3 session.py ] or use repl.it (required)
    SESSION = getenv("SESSION")
    # access token of your bot, without this the bot will not work (required)
    BOT_TOKEN = getenv("BOT_TOKEN")
    # database url (required)
    DB_URI = getenv("DATABASE_URL", "sqlite:///tron.db")
    # a group to store logs, etc (required)
    LOG_CHAT = int(getenv("LOG_CHAT", "-100"))
