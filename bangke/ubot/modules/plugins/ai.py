import requests
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
# Tentukan teks yang ingin Anda cari
text = "Halo dunia"

# Tentukan kunci API Anda
api_key = "LwulPck3"

# Buat permintaan GET ke API
url = "https://api.botcahx.eu.org/api/search/blackbox-chat"
params = {"text": text, "apikey": api_key}
response = requests.get(url, params=params)

# Periksa apakah permintaan berhasil
if response.status_code == 200:
    # Respons berisi daftar hasil pencarian
    results = response.json()["results"]

    # Cetak hasil pencarian
    for result in results:
        print(result["title"])
        print(result["description"])
        print(result["text"])
else:
    # Ada kesalahan dengan permintaan
    print("Terjadi kesalahan saat mengambil hasil pencarian.")