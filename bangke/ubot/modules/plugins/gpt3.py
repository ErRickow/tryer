import json

import requests
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from bangke import app, gen

url = "https://abot3.gchk2.skybyte.me/api/chat-process"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "id-ID,id;q=0.9",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://abot3.gchk2.skybyte.me",
    "priority": "u=1, i",
    "referer": "https://abot3.gchk2.skybyte.me/",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}
