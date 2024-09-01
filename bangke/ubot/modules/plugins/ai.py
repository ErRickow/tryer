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

    # Buat permintaan GET ke API
    url = "https://api.botcahx.eu.org/api/search/blackbox-chat"
    params = {"text": text, "apikey": "YOUR_API_KEY"}
    response = requests.get(url, params=params)

    # Periksa apakah permintaan berhasil
    if response.status_code == 200:
        # Respons berisi daftar hasil pencarian
        try:
            results = response.json()["results"]
        except KeyError:
            await message.reply_text("Terjadi kesalahan saat mengambil hasil pencarian.")
            return

        # Jika tidak ada hasil, beri tahu pengguna
        if not results:
            await message.reply_text("Tidak ada hasil yang ditemukan.")
            return

        # Kirim hasil pencarian ke pengguna
        for result in results:
            await message.reply_text(f"**{result['title']}**\n{result['description']}\n{result['text']}")
    else:
        # Ada kesalahan dengan permintaan
        await message.reply_text("Terjadi kesalahan saat mengambil hasil pencarian.")