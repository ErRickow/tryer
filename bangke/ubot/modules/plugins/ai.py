import requests
import json
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from bangke import app
from bangke.core import filters
from bangke.core.enums import HandlerType

@app.on_update(
    handler_type=HandlerType.MESSAGE,
    filters=filters.gen(
        commands="ai",
        usage="tanya dengan ai."
    )
)
async def ai(client: Client, message: Message):
    if len(message.command) > 1:
        text = message.text.split(maxsplit=1)[1]
    else:
        await message.reply_text("Ketik sesuatu untuk ditanyakan!")
        return

    # Buat permintaan POST ke API
    url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
    headers = {"Content-Type": "application/json"}
    data = {"message": text}
    response = requests.post(url, headers=headers, json=data)

    # Periksa apakah permintaan berhasil
    if response.status_code == 200:
        # Respons berisi jawaban dari ChatGPT
        try:
            answer = response.json()["response"]
        except KeyError:
            await message.reply_text("Terjadi kesalahan saat mengambil jawaban.")
            return

        # Kirim jawaban ke pengguna
        await message.reply_text(answer)
    else:
        # Ada kesalahan dengan permintaan
        await message.reply_text("Terjadi kesalahan saat mengambil jawaban.")