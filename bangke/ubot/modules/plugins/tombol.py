""" power plugin """

import os
import sys
import time

from pyrogram.types import Message

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
        msg = await app.send_edit("Restarting bot . . .", text_type=["mono"])

        os.execv(sys.executable, ['python'] + sys.argv)
        await app.edit_message_text(
            msg.chat.id,
            msg.message_id,
            "Restart completed !\nBot is alive now !"
        )
    except Exception as e:
        await m.edit("Failed to restart userbot !", delme=2, text_type=["mono"])
        await app.error(e)




@app.on_cmd(
    commands="sleep",
    usage="Make your bot sleep.",
    disable_for=UserType.SUDO
)
async def sleep_handler(_, m: Message):
    """ sleep handler for power plugin """
    if app.long() == 1:
        return await app.send_edit("Berikan detik juga kontol. . .")

    elif app.long() > 1:
        arg = m.command[1]

    if arg.isdigit():
        cmd = int(arg)
        if cmd > 86400:
            return await app.send_edit(
                "Sorry ye ,lu gabisa nidurin bot selama (> 86400 detik) . . .",
                text_type=["mono"],
                delme=3
            )

        formats = {
            cmd<60:f"{cmd} detik",
            cmd>=60:f"{cmd//60} menit",
            cmd>=3600:f"{cmd//3600} jam"
            }

        suffix = "`null`"
        for x in formats: # very small loop
            if x:
                suffix = formats[x]
                break

        await app.send_edit(f"Tidur selama {suffix} . . .", delme=cmd)
        time.sleep(cmd)
    else:
        await app.send_edit("Berikan angka bukan teks ,bangsatt!! . . .", delme=3, text_type=["mono"])
