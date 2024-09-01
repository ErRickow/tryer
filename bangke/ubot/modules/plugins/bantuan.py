""" help plugin """

import os
from pyrogram import filters
from pyrogram.types import Message, InlineQueryResultPhoto, InlineKeyboardMarkup
from pyrogram.errors import BotInlineDisabled
from bangke import app, gen

@app.on_cmd(
    commands="help",
    usage="Get your helpmenu, use plugin name as suffix to get command information.",
)
async def helpmenu_handler(_, m: Message):
    """ helpmenu handler for help plugin """

    args = m.command or m.sudo_message.command or []

    try:
        if len(args) <= 1:
            await app.send_edit(". . .")

            # Mengambil hasil inline query
            result = await app.get_inline_bot_results(app.bot.username, "#help")
            if result and result.results:
                await m.delete()
                await app.send_inline_bot_result(
                    m.chat.id,
                    query_id=result.query_id,
                    result_id=result.results[0].id,
                    disable_notification=True,
                )
            else:
                await app.send_edit(
                    "Please check if your bot's inline mode is on . . .",
                    delme=3
                )
        else:
            module_help = await app.PluginData(args[1])
            if not module_help:
                await app.send_edit(
                    f"Invalid plugin name specified, use {app.Trigger()[0]}uplugs to get list of plugins",
                    delme=3
                )
            else:
                await app.send_edit(f"MODULE: {args[1]}\n\n" + "".join(module_help))
    except BotInlineDisabled:
        await app.toggle_inline()
        await helpmenu_handler(_, m)
    except Exception as e:
        await app.error(e)


@app.bot.on_inline_query(filters.user(app.AllUsersId))
async def inline_result(_, inline_query):
    print(inline_query)
    query = inline_query.query
    emoji = app.HelpEmoji or "•"

    if query.startswith("#help"):
        await inline_query.answer(
            results=[
                InlineQueryResultPhoto(
                    photo_url=app.BotPic,
                    title="Tron Inline helpdex menu",
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
