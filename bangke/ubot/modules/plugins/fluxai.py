import io
import time

import requests
from PIL import Image
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import *

from bangke import app, gen
from bangke import *

async def schellwithflux(args):
    API_URL = "https://randydev-ryuzaki-api.hf.space/api/v1/akeno/fluxai"
    payload = {
        "user_id": 1191668125,  # Please don't edit here
        "args": args
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code != 200:
        message.reply(f"Error status {response.status_code}")
        return None
    return response.content


@app.on_cmd(
    commands=["fluxai", "flux"],
    usage="Get userbot response time."
)

async def imgfluxai_(client: Client, message: Message):
    question = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not question:
        return await message.reply_text("Please provide a question for Flux.")
    try:
        image_bytes = await schellwithflux(question)
        if image_bytes is None:
            return await message.reply_text("Failed to generate an image.")
        pro = await message.reply_text("Generating image, please wait...")
        with open("flux_gen.jpg", "wb") as f:
            f.write(image_bytes)
        ok = await pro.edit_text("Uploading image...")
        await message.reply_photo("flux_gen.jpg", progress=progress, progress_args=(ok, time.time(), "Uploading image..."))
        await ok.delete()
        if os.path.exists("flux_gen.jpg"):
            os.remove("flux_gen.jpg")
    except Exception as e:
        LOGS.error(str(e))
        await message.edit_text(str(e))
