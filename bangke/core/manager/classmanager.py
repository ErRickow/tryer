import time
import logging
import platform

from requests.exceptions import ConnectionError
from bangke import Config
from telegraph import Telegraph
from pyrogram import __version__ as pyrogram_version
from bangke.core.methods import Methods



class ClassManager(Config, Methods):
    # versions /
    python_version = str(platform.python_version())
    pyrogram_version = str(pyrogram_version)

    # assistant /
    assistant_name = "Nora"
    assistant_version = "v.0.0.5"

    # userbot /
    userbot_name = "Tron"
    userbot_version = "v.0.2.0"

    # containers /
    CMD_HELP = {}

    # owner details /
    owner_name = "࿇•ẞᗴᗩSԵ•࿇"
    owner_id = 1790546938
    owner_username = "@BEASTZX"

    # other /
    message_ids = {}
    PIC = "https://telegra.ph/file/38eec8a079706b8c19eae.mp4"
    Repo = "https://github.com/TronUb/Tron.git"
    StartTime = time.time()
    utube_object = object
    callback_user = None
    whisper_ids = {}

    # debugging /


    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.session.internals.msg_id").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.connection.connection").setLevel(logging.WARNING)
    log = logging.getLogger()

    # telegraph /
    try:
        telegraph = Telegraph()
        telegraph.create_account(short_name=Config.TL_NAME or "TronUserbot Team")
    except (ConnectionError, AttributeError):
        telegraph = None

