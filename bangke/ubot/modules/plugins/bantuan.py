""" help plugin """

import os

from pyrogram import filters, Client
from pyrogram.errors import BotInlineDisabled

from bangke import app, gen

from pyrogram.types import Message, InlineQueryResultArticle, InputTextMessageContent

@app.on_cmd(
    commands="help",
    usage="Get your help menu, use plugin name as suffix to get command information.",
)
async def helpmenu_handler(_, m: Message):
    """ Help menu handler for help plugin """

    args = m.command or m.sudo_message.command or []
    args_exists = len(args) > 1

    try:
        if not args_exists:
            await app.send_edit(". . .", text_type=["mono"])
            # Menampilkan bantuan umum secara langsung
            help_text = "Use /help <plugin_name> to get specific help."
            await m.reply(help_text)
        else:
            module_help = await app.PluginData(args[1])
            if not module_help:
                await app.send_edit(
                    f"Invalid plugin name specified, use {app.Trigger()[0]}plugs to get the list of plugins",
                    delme=3
                )
            else:
                await app.send_edit(f"MODULE: {args[1]}\n\n" + "".join(module_help))
    except Exception as e:
        await app.error(e)

@app.on_inline_query()
async def inline_help_query(client, query):
    """ Handle inline queries for help """
    
    # Ambil plugin yang diminta dari query
    plugin_name = query.query.strip()
    
    # Jika tidak ada nama plugin, tampilkan daftar bantuan umum
    if not plugin_name:
        results = [
            InlineQueryResultArticle(
                title="Help Menu",
                description="Get help for specific commands.",
                input_message_content=InputTextMessageContent("Use /help <plugin_name> for specific help.")
            ),
        ]
        await client.answer_inline_query(query.id, results)
        return
    
    # Ambil data plugin berdasarkan nama
    module_help = await app.PluginData(plugin_name)
    
    if module_help:
        results = [
            InlineQueryResultArticle(
                title=f"Help for {plugin_name}",
                description="\n".join(module_help),
                input_message_content=InputTextMessageContent("\n".join(module_help))
            )
        ]
    else:
        results = [
            InlineQueryResultArticle(
                title="Error",
                description="Invalid plugin name specified.",
                input_message_content=InputTextMessageContent("No help found for this plugin.")
            )
        ]
    
    await client.answer_inline_query(query.id, results)

app.run()


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
