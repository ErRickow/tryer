from pyrogram import filters

from pyrogram.types import (
    InlineKeyboardMarkup, 
    Message,
)

from bangke.ubot.client import app





emoji = app.HelpEmoji or "•"

settings = app.BuildKeyboard(([f"{emoji} Settings {emoji}", "settings-tab"], [f"{emoji} Modules {emoji}", "plugins-tab"]))
extra = app.BuildKeyboard(([f"{emoji} Extra {emoji}", "extra-tab"], [f"{emoji} Stats {emoji}", "stats-tab"]))
about = app.BuildKeyboard(([["Assistant", "assistant-tab"]]))
close = app.BuildKeyboard(([["Close", "close-tab"]]))
public = app.BuildKeyboard(([[f"{emoji} Public Commands {emoji}", "public-commands-tab"]]))





# /help command for bot
@app.bot.on_message(filters.command("help"), group=-1)
async def bot_start_handler(_, m: Message):
    if m.from_user:
        if m.from_user.id == app.id:
            # Bot sendiri
            buttons = InlineKeyboardMarkup(
                [settings, extra, about, close]
            )
            await app.bot.send_message(
                m.chat.id,
                app.BotBio(m),
                reply_markup=buttons
            )

        elif m.from_user.id != app.id:
            await app.bot.send_message(
                m.chat.id,
                f"Allo {m.from_user.mention}, lu pantas menggunakan gw. Ada beberapa commands yang bisa lu pake. Liat di bawah.",
                reply_markup=InlineKeyboardMarkup(
                    [public]
                ),
            )