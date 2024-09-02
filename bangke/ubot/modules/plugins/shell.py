import re
import sys
import traceback
import subprocess

from io import StringIO

from pyrogram.types import Message

from bangke import app, gen
from bangke.core.enums import UserType

@app.on_cmd(
    commands=["term", "shell"],
    usage="Execute shell scripts.",
    disable_for=UserType.SUDO
)
async def terminal_handler(_, m: Message):
    """ This function is made to run shell commands """

    try:
        if app.long() == 1:
            return await app.send_edit("Use: `.term pip3 install colorama`", delme=5)

        await app.send_edit("Running in shell . . .", text_type=["mono"])
        text = m.sudo_message.text if getattr(m, "sudo_message", None) else m.text
        pattern = """ (?=(?:[^'"]|'[^']*'|"[^"]*")*$)"""
        cmd = m.text.split(None, 1)[1]

        if "\n" in cmd:
            code = cmd.split("\n")
            output = ""
            for command in code:
                shell = re.split(pattern, command)
                try:
                    process = subprocess.Popen(
                        shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                except Exception as e:
                    await app.error(e)

                output += "**{code}**\n"
                output += process.stdout.read()[:-1].decode("utf-8")
                output += "\n"
        else:
            shell = re.split(pattern, cmd)
            for y in range(len(shell)):
                shell[y] = shell[y].replace('"', "")

            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                errors = traceback.format_exception(
                    etype=exc_type, value=exc_obj, tb=exc_tb
                )
                return await app.send_edit(f"**Error:**\n\n`{''.join(errors)}`")

            output = process.stdout.read()[:-1].decode("utf-8")
        if str(output) == "\n":
            output = None

        if output:
            if len(output) > 4096:
                await app.create_file(
                    filename="term_output.txt",
                    content=output,
                    caption=f"`{cmd}`"
                )
            else:
                await app.send_edit(f"**COMMAND:**\n\n`{cmd}`\n\n\n**OUTPUT:**\n\n`{output}`")
        else:
            await app.send_edit(f"**COMMAND:**\n\n`{cmd}`\n\n\n**OUTPUT:**\n\n`No Output`")
    except Exception as e:
        await app.error(e)
