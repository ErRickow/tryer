import asyncio
import os
from json import tool

import cohere
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from bangke import app
from bangke.core import filters
from bangke.core.enums import HandlerType

@app.on_update(
    handler_type=HandlerType.MESSAGE,
    filters=filters.gen(
        commands="cohere",
        usage="tanya dengan ai."
    )
)
async def coheres_(c: Client, message: Message):
    co = cohere.Client(api_key=hPZY8Tf8TXUZRK3jzuOZyz0atWR9q7IzywrK4hTQ)
    try:
        if len(message.command) > 1:
            prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
            prompt = message.reply_to_message.text
        else:
            await message.reply_text(
                "<b>Usage: </b><code>.cohere [prompt/reply to message]</code>"
            )
            return
        response = co.chat(
            prompt=prompt,
            model="command-r-plus"
        )
        output = response.text
        if len(output) > 4096:
            with open("chat.txt", "w+", encoding="utf8") as out_file:
                out_file.write(output)
            await message.reply_document(
                document="chat.txt",
                disable_notification=True
            )
            os.remove("chat.txt")
        else:
            await message.reply_text(output, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
