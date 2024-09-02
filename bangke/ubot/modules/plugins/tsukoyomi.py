import os
import asyncio

from pyrogram.types import Message

from pyrogram import Client, filters
from bangke import app, gen
from bangke.core.enums import UserType 



@app.on_cmd(
    commands="tsukoyomi",
    usage="Check deleted accounts in chat, use clean as suffix to remove them.",
    disable_for=UserType.SUDO
)
async def zombies_handler(client, message):
    if await app.check_private():
        return

    temp_count = 0
    admin_count = 0
    count = 0

    if app.long() != 2:
        a = await message.reply("Sedang mngendus . . .", quote=True)

        async for x in app.get_chat_members(chat_id=message.chat.id):
            if x.user.is_deleted:
                temp_count += 1

        if temp_count > 0:
            await a.edit_text(f"Terdeteksi {temp_count} Musuhnya Bapak Naruto\nGunakan {app.Trigger[0]}tsukoyomi untuk melenyapkannya dari bumi.", quote=True)
        else:
            await a.edit_text("KGA ADA MUSUH YANG TERDETEKSI EMHH.\nGroup bersih nan sentosa ! 😃", quote=True)

    elif app.long() == 2 and message.command[1] == "kyaa":
        await a.edit_text("*SHINRA TENSEI* . . .", quote=True)

        async for x in app.get_chat_members(chat_id=message.chat.id):
            if x.user.is_deleted:
                if x.status in ("administrator", "creator"):
                    admin_count += 1
                    continue
                try:
                    await app.ban_chat_member(
                        chat_id=message.chat.id,
                        user_id=x.user.id
                    )
                    count += 1
                    await asyncio.sleep(0.2)
                except Exception as e:
                    await app.error(e)
        await a.edit_text(f"WATASHIWA DONE\n\n*Total:* {count+admin_count}\n*Removed:* {count}\n*Not Removed:* {admin_count}\n\n*Note:* Not removed accounts can be admins or the owner", quote=True)

    elif app.long() == 2 and message.command[1] != "kyaa":
        await a.edit_text(f"Check {app.Trigger[0]}help tsukoyomi` to see how it works !", quote=True)
    else:
        await a.edit_text("Something went wrong, please try again later !", quote=True)