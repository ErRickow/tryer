import os
from bangke.others import Colors


try:
    import uvloop
    uvloop.install()
except ImportError:
    print(f"{Colors.red}\nuvloop wasn't installed, userbot will work slow.{Colors.reset}\n")

from bangke.ubot.client.client import SuperClient


app = SuperClient()
