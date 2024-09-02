import os
import sys
import time

from pyrogram.types import Message
from pyrogram import Client

from bangke import app, gen
from bangke.core.enums import UserType

@app.on_cmd(
    commands="reboot",
    usage="Reboot your userbot.",
    disable_for=UserType.SUDO
)
async def reboot_handler(_, m: Message):
    """ reboot handler for power plugin """
    try:
        msg = await m.reply("Restarting bot . . .", quote=True, text_type=["mono"])

        os.execv(sys.executable, ['python'] + sys.argv)
        await app.edit_message_text(
            msg.chat.id,
            msg.message_id,
            "Restart completed !\nBot is alive now !"
        )
    except Exception as e:
        await m.reply("Failed to restart userbot !", quote=True, delme=2, text_type=["mono"])
        await app.error(e)


@app.on_cmd(
    commands="tidur",
    usage="Make your bot sleep.",
    disable_for=UserType.SUDO
)
async def sleep_handler(client: Client, m: Message):
    """ sleep handler for power plugin """
    if app.long() == 1:
        return await m.reply("Berikan angka juga kontol. . .", quote=True)

    elif app.long() > 1:
        arg = m.command[1]

    if arg.isdigit():
        cmd = int(arg)
        if cmd > 86400:
            return await m.reply(
                "Sorry ye ,lu gabisa nidurin bot selama (> 86400 detik) . . .",
                quote=True,
                text_type=["mono"],
                delme=3
            )

        formats = {
            cmd<60:f"{cmd} detik",
            cmd>=60:f"{cmd//60} menit",
            cmd>=3600:f"{cmd//3600} jam"
            }

        suffix = "null"
        for x in formats: # very small loop
            if x:
                suffix = formats[x]
                break

        await m.reply(f"Tidur selama {suffix} . . .", quote=True, delme=cmd)
        time.sleep(cmd)
    else:
        await m.reply("Berikan angka bukan teks ,bangsatt!! . . .", quote=True, delme=3, text_type=["mono"])