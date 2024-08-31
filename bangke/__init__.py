import os
import socket
import platform
import subprocess
from importlib import metadata
from bangke.others import Colors
from config import Configuration


# Check which packages are installed
installed_python_libs = [package.metadata["Name"].lower() for package in metadata.distributions()]


class Config:
    """This class generates the configs"""
    pass


def isLocalHost():
    """Check if it is localhost"""
    return os.path.exists("config.txt")


class Tools:
    """Use it for installing the required packages"""
    device = platform.uname()[0].lower()
    is_linux = device == "linux"
    is_windows = device == "windows"

    @property
    def clear_screen(self):
        os.system("clear" if self.is_linux else "cls")

    def check_command(self, args: list):
        return subprocess.run(
            args,
            stdout=subprocess.PIPE,
            shell=True,
            check=True
        ).stdout.decode()

    def setup_config(self):
        count = 1
        #self.clear_screen()  # Call the method

        # Check if the user config file exists
        if os.path.isfile("config.txt"):
            print("config.txt file exists: Yes\n\n")
            with open("config.txt") as f:
                content = [x for x in f.read().split("\n") if x.strip()]

            # Set text file config values
            print(Colors.block + "Setting configuration values.\n\n" + Colors.reset)
            for x in content:
                data = x.split("=")
                if len(data) < 2:  # Check if we have at least two elements
                    print(f"Skipping invalid configuration line: {x}")
                    continue

                file_value = data[1].strip()
                if file_value.isdigit():
                    file_value = int(file_value)

                setattr(Config, data[0].strip(), file_value)  # Strip key as well
                print(f"[{count}] Added config = {data[0].strip()} with value = {file_value}\n")
                count += 1

        else:
            print("config.txt file doesn't exist, exiting...")
            exit(0)

        # Set remaining necessary config values
        print(Colors.block + "\nSetting remaining configuration values\n\n" + Colors.reset)
        for attr in dir(Configuration):
            value = getattr(Configuration, attr, None)

            if attr.isupper() and not hasattr(Config, attr):
                setattr(Config, attr, value)
                print(f"[{count}] Added config = {attr} with value = {value}\n")
                count += 1

        clear = input(f"{Colors.block}Should I clear the screen?{Colors.reset} (Y/N): ")
        if not clear or (clear.upper() == "Y"):
            self.clear_screen()  # Call the method


tools = Tools()

if isLocalHost():
    tools.setup_config()
else:
    print("Setting the Non-LocalHost setup ... !")
    for attr in dir(Configuration):
        value = getattr(Configuration, attr, None)
        if attr.isupper() and not hasattr(Config, attr):
            setattr(Config, attr, value)

# Default import
from bangke.ubot import app
bot = app.bot
from bangke.core.filters import gen