import io
import time

import requests
from PIL import Image
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import *

from bangke import app, gen
from config import *

async def schellwithflux(message, args):
    API_URL = "https://randydev-ryuzaki-api.hf.space/api/v1/akeno/fluxai"
    payload = {
        "user_id": 1191668125,  # Please don't edit here
        "args": args
    }
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content
    except requests.RequestException as e:
        await message.reply_text(f"Error: {str(e)}")
        return None

@app.on_cmd(
    commands=["fluxai", "flux"],
    usage="Get userbot response time."
)
async def imgfluxai_(client: Client, message: Message):
    question = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not question:
        return await message.reply_text("Please provide a question for Flux.")
    
    image_bytes = await schellwithflux(message, question)  # Pass message here
    if image_bytes is None:
        return  # Error already handled in schellwithflux

    pro = await message.reply_text("Generating image, please wait...")
    
    with open("flux_gen.jpg", "wb") as f:
        f.write(image_bytes)
    
    ok = await pro.edit_text("Uploading image...")
    await message.reply_photo("flux_gen.jpg", progress=progress, progress_args=(ok, time.time(), "Uploading image..."))
    await ok.delete()
    
    if os.path.exists("flux_gen.jpg"):
        os.remove("flux_gen.jpg")