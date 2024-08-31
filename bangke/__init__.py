""" everything starts here """

import os
import socket
import platform
import subprocess
from importlib import metadata
from bangke.others import Colors
from config import Configuration


# check which packages are installed
installed_python_libs = []

for package in metadata.distributions():
    installed_python_libs.append(package.metadata["Name"].lower())




class Config:
    """This class generates the configs """
    pass


def isLocalHost():
    """Check if it is localhost"""
    return os.path.exists("config.txt")


class Tools:
    """Use it for installing the required packages """
    device = platform.uname()[0].lower()
    is_linux = device=="linux"
    is_windows = device=="windows"

    @property
    def clear_screen(self):
        os.system("clear" if self.is_linux else "cls")

    def check_command(self, args: list):
        return (subprocess.run(
            args,
            stdout=subprocess.PIPE,
            shell=True,
            check=True
        )).stdout.decode()

        def setup_config(self):
          count = 0
          self.clear_screen

        # check requirements & install
       # self.check_requirements()
       # self.clear_screen

        # check if the user config file exists
        if os.path.isfile("config.txt"):
            print("config.txt file exists: Yes\n\n")
            with open("config.txt") as f:
                content = [x for x in f.read().split("\n") if x.strip()]

            # set text file config values
            print(Colors.block + "Setting configuration values.\n\n" + Colors.reset)
            for x in content:
                data = x.split("=")
                file_value = data[1]
                if len(data) < 2:
                  
                  print(f"skipping invalid configuration value line: {x}")
                  continue
                file_value = data[1].strip()
                if file_value.isdigit():
                  file_value = int(file_value)

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
            self.clear_screen



tools = Tools()

if(isLocalHost()):
    tools.setup_config()
else:
    print("Setting the Non-LocalHost setup ... !")
    for attr in dir(Configuration):
        value = getattr(Configuration, attr, None)
        if attr.isupper() and not hasattr(Config, attr):
            setattr(Config, attr, value)


# default import
from main.userbot import app
bot = app.bot
from main.core.filters import gen
