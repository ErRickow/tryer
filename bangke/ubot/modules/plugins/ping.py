import random
import asyncio

from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import *

from bangke import app, gen



# animations
data = [
    "🕜",
    "🕡",
    "🕦",
    "🕣",
    "🕥",
    "🕧",
    "🕓",
    "🕔",
    "🕒",
    "🕑",
    "🕐"
]

pings = []


@app.on_cmd(
    commands=["ping", "pong"],
    usage="Get userbot response time."
)
async def ping_handler(client: Client, m: Message):
    """ ping handler for ping plugin """
    try:

        if app.long() == 1:
            start = datetime.now()
            await m.reply(". . .", text_type=["mono"])
            end = datetime.now()
            m_s = (end - start).microseconds / 1000
            await m.reply(
                f"**Pöng !**\n`{m_s} ms`\n⧑ {app.UserMention}",
                disable_web_page_preview=True
            )
        elif app.long() == 2:
            cmd = m.command
            count = int(cmd[1]) if cmd[1] and cmd[1].isdigit() else 0
            if count <= 1:
                return await app.send_edit(
                    f"Use `{app.Trigger[0]}ping` for pings less than 1.",
                    delme=3
                )

            else:
                try:
                    for _ in range(count):
                        await infinite()
                        await app.send_edit(". . .", text_type=["mono"])
                        await asyncio.sleep(0.30)
                    await app.send_edit("".join(pings))
                    pings.clear()
                except Exception as e:
                    await app.error(e)
        else:
            return await app.send_edit("Something went wrong in ping module.", delme=2)
    except Exception as e:
        await app.error(e)




# function to create lots of pings
async def infinite():
    """ infinite function for ping plugin """
    start = datetime.now()
    await app.send_edit(random.choice(data)) # MessageNotModified
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    msg = f"Pöng !\n{m_s} ms\n⧑ {app.UserMention}\n\n"
    pings.append(msg)
    return True