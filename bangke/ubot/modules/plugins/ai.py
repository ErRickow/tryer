import requests
import json
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from bangke import app
from bangke.core import filters
from bangke.core.enums import HandlerType

async def chatgptold(messagestr):
    url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
    payload = {"query": messagestr}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        return None
    return response.json()

@app.on_update(
    handler_type=HandlerType.MESSAGE,
    filters=filters.gen(
        commands="ai",
        usage="tanya dengan ai."
    )
)
async def chatgpt_old_(client: Client, message: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        return await message.reply_text("Give ask from CHATGPT-3")
    try:
        messager = await chatgptold(prompt)
        if messager is None:
            return await message.reply_text("No response")
        output = messager["randydev"].get("message")
        if len(output) > 4096:
            with open("chat.txt", "w+", encoding="utf8") as out_file:
                out_file.write(output)
            await message.reply_document(
                document="chat.txt",
                disable_notification=True
            )
            os.remove("chat.txt")
        else:
            await message.reply_text(output)
    except Exception as e:
        LOGS.error(str(e))
        return await message.reply_text(str(e))
