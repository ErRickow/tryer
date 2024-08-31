from pyrogram import filters
from pyrogram.types import CallbackQuery

from bangke.ubot.client import app





@app.bot.on_callback_query(filters.regex("update-tab"))
@app.alert_user
async def update_callback(_, cb: CallbackQuery):
    await cb.answer(
        text="Fiturnya belum ada anjing tolol.",
        show_alert=True
    )
