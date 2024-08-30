import os
import socket
import platform
import subprocess
#from importlib import metadata
from bangke.others import Colors
from config import Configuration

class Config:
    """This class generates the configs """
    pass


def isLocalHost():
    """Check if it is localhost"""
    return os.path.exists("config.txt")
    
class Tools:

        # check if the user config file exists
    def setup_config(self):
        count = 1
        #self.clear_screen

        # check requirements & install
      #  self.check_requirements()
      #  self.clear_screen

        # check if the user config file exists
        if os.path.exists("config.txt"):
            print("config.txt file exists: Yes\n\n")
            with open("config.txt") as f:
                content = [x for x in f.read().split("\n") if x not in ("\n", "")]

            # set text file config values
            print(Colors.block + "Setting configuration values.\n\n" + Colors.reset)
            for x in content:
                data = x.split("=")
                file_value = data[0]
                if data[0].isdigit():
                    file_value = int(data[0])

                setattr(Config, data[0], file_value)
                print(f"[{count}] Added config = {data[0]} with value = {file_value}\n")
                count += 1

        else:
            print("config.txt file doesn't exist, existing. . .")
            exit(0)

        # set remaining necessary config values
        print(Colors.block + "\nSetting remaining configuration values\n\n" + Colors.reset)
        for attr in dir(Configuration):
            value = getattr(Configuration, attr, None)

            if attr.isupper() and not hasattr(Config, attr):
                setattr(Config, attr, value)
                print(f"[{count}] Added config = {attr} with value = {value}\n")
                count += 1

        clear = input(f"{Colors.block}Should I clear the screen ?{Colors.reset} (Y/N): ")
        if (not clear) or (clear and clear.upper() == "Y"):
           # self.clear_screen



           tools = Tools()

if(isLocalHost()):
    Tools.setup_config()
else:
    print("Setting the Non-LocalHost setup ... !")
    for attr in dir(Configuration):
        value = getattr(Configuration, attr, None)
        if attr.isupper() and not hasattr(Config, attr):
            setattr(Config, attr, value)


# default import
from bangke.ubot import app
bot = app.bot
from bangke.core.filters import gen
