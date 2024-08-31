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
        # Hanya jalankan jika perlu
        if args:
            return subprocess.run(
                args,
                stdout=subprocess.PIPE,
                shell=True,
                check=True
            ).stdout.decode()
        return None

    def setup_config(self):
        count = 1

        # Cek apakah file konfigurasi ada
        if os.path.isfile("config.txt"):
            print("config.txt file exists: Yes\n\n")
            with open("config.txt") as f:
                content = [x.strip() for x in f if x.strip()]

            # Set nilai konfigurasi dari file
            print(Colors.block + "Setting configuration values.\n\n" + Colors.reset)
            for x in content:
                data = x.split("=")
                if len(data) < 2:  # Cek jika ada setidaknya dua elemen
                    print(f"Skipping invalid configuration line: {x}")
                    continue

                file_value = data[1].strip()
                if file_value.isdigit():
                    file_value = int(file_value)

                setattr(Config, data[0].strip(), file_value)  # Strip key juga
                print(f"[{count}] Added config = {data[0].strip()} with value = {file_value}\n")
                count += 1

        else:
            print("config.txt file doesn't exist, exiting...")
            exit(0)

        # Set nilai konfigurasi yang diperlukan
        print(Colors.block + "\nSetting remaining configuration values\n\n" + Colors.reset)
        for attr in dir(Configuration):
            value = getattr(Configuration, attr, None)

            if attr.isupper() and not hasattr(Config, attr):
                setattr(Config, attr, value)
                print(f"[{count}] Added config = {attr} with value = {value}\n")
                count += 1

        # Menghilangkan prompt untuk clear screen
         self.clear_screen()  # Call the method jika ingin membersihkan layar otomatis

# Pastikan untuk mendefinisikan Config dan Configuration di sini.

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