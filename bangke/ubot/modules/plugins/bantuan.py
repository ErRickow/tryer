""" help plugin """

import os

from pyrogram import filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
    WebAppInfo
)
from telegraph.exceptions import RetryAfterError
from pyrogram.errors import BotInlineDisabled

from bangke import app, gen

@app.bot.on_inline_query(filters.user(app.AllUsersId))
async def inline_result(_, inline_query):
    print(inline_query)
    query = inline_query.query
    if query.startswith("#asu"):
        emoji = app.HelpEmoji or "•"

        await inline_query.answer(
        results=[
            InlineQueryResultPhoto(
                photo_url=app.BotPic,
                title="Er Userbot",
                description="Get your inline helpdex menu.",
                caption=app.home_tab_string,
                reply_markup=InlineKeyboardMarkup(
                    [
                        app.BuildKeyboard(
                            (
                                [f"{emoji} Settings {emoji}", "settings-tab"],
                                [f"{emoji} Plugins {emoji}", "plugins-tab"]
                            )
                        ),
                        app.BuildKeyboard(
                            (
                                [f"{emoji} Extra {emoji}", "extra-tab"],
                                [f"{emoji} Stats {emoji}", "stats-tab"]
                            )
                        ),
                        app.BuildKeyboard(([["Assistant", "assistant-tab"]])),
                        app.BuildKeyboard(([["Close", "close-tab"]]))
                    ]
                )
            )
        ],
        cache_time=1
        )


# get all module name
@app.on_cmd(
    commands="uplugs",
    usage="Get list of userbot plugin names."
)
async def uplugs_handler(_, m: Message):
    """ uplugs handler for help plugin """
    store = []
    store.clear()
    for x in os.listdir("bangke/ubot/modules/plugins/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit("**PLUGINS OF USERBOT:**\n\n" + "".join(store))




# get all plugins name
@app.on_cmd(
    commands="bplugs",
    usage="Get list of your bot plugin names."
)
async def aplugs_handler(_, m: Message):
    """ aplugs handler for help plugin """
    store = []
    store.clear()
    for x in os.listdir("bangke/assistant/modules/plugins/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit("**PLUGINS OF ASSISTANT:**\n\n" + "".join(store))




@app.on_cmd(
    commands="inline",
    usage="Toggle on/off inline mode of bot."
)
async def toggleinline_handler(_, m: Message):
    """ toggleinline handler for help plugin """
    return await app.toggle_inline()
