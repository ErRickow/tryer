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
        commands="ask",
        usage="tanya dengan ai."
    )
)
async def ai(client: Client, message: Message):
  text = "Halo dunia"
  api_key = "LwulPck3"

  # Buat permintaan GET ke API
  url = "https://api.botcahx.eu.org/api/search/blackbox-chat"
  params = {"text": text, "apikey": api_key}
  response = requests.get(url, params=params)

  # Periksa apakah permintaan berhasil
  if response.status_code == 200:
    # Respons berisi daftar hasil pencarian
    try:
      results = response.json()["results"]
    except KeyError:
      await message.reply_text("Terjadi kesalahan saat mengambil hasil pencarian.")
      return

    # Cetak hasil pencarian
    for result in results:
        await message.reply_text(f"**{result['title']}**\n{result['description']}\n{result['text']}")
  else:
    # Ada kesalahan dengan permintaan
    await message.reply_text("Terjadi kesalahan saat mengambil hasil pencarian.")