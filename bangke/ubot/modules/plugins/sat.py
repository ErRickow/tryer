import asyncio
import random
import time
from datetime import datetime as dt

from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.types import Message

from bangke import app, gen

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += f"{time_list.pop()}, "

    time_list.reverse()
    readable_time += ":".join(time_list)

    return readable_time

PING_TEMPLATES = [
"""
🔷  **Speed:** {speed} m/s
🔷  **Uptime:** {uptime}
🔷  **Onwer:** {owner}
""",
]

async def ping_template(speed: float, uptime: str, owner: str) -> str:
    message = random.choice(PING_TEMPLATES)
    return message.format(speed=speed, uptime=uptime, owner=owner)

StartTime = time.time()

@app.on_cmd(
    commands=["kping", "blop"],
    usage="Get userbot response time."
)
async def ping(client: Client, message: Message):
    start_time = time.time()
    pro = await message.reply_text("**Pong !!**")
    uptime = get_readable_time(time.time() - StartTime)
    #img = await db.get_env(ENV_TEMPLATE.ping_pic)
    end_time = time.time()
    speed = end_time - start_time
    caption = await ping_template(round(speed, 3), uptime, app.UserMention)
    try:
      await message.reply_photo(
        img,
        caption=caption,
        )
        await pro.delete()
        return
      await pro.edit_text(caption)
