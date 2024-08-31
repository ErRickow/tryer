""" help plugin """

import os

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import BotInlineDisabled

from bangke import app, gen



@app.on_cmd(
    commands="help",
    usage="Get your helpmenu, use plugin name as suffix to get command information.",
)
async def helpmenu_handler(_, m: Message):
    """ helpmenu handler for help plugin """

args = m.command or m.sudo_message.command or []
args_exists = len(args) > 1  # Ubah menjadi boolean langsung

try:
    if not args_exists:
        await app.send_edit(". . .", text_type=["mono"])
        result = await app.get_inline_bot_results(
            app.bot.username,
            "#helpmenu"
        )
        # Tambahkan pemeriksaan untuk result
        if result and result.results:
            await m.delete()
            info = await app.send_inline_bot_result(
                m.chat.id,
                query_id=result.query_id,
                result_id=result.results[0].id,
                disable_notification=True,
            )
        else:
            await app.send_edit(
                "Tidak ada hasil ditemukan untuk inline help.",
                delme=3,
                text_type=["mono"]
            )
    elif args_exists:
        # Logika untuk menangani argumen kedua
        module_help = await app.PluginData(args[1])
        if not module_help:
            await app.send_edit(
                f"Nama plugin tidak valid, gunakan {app.Trigger()[0]}uplugs untuk mendapatkan daftar plugin",
                delme=3
            )
        else:
            await app.send_edit(f"MODULE: {args[1]}\n\n" + "".join(module_help))
    else:
        await app.send_edit("Coba lagi nanti!", text_type=["mono"], delme=3)
except BotInlineDisabled:
    await app.toggle_inline()
    await helpmenu_handler(_, m)
except Exception as e:
    await app.error(e)



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
