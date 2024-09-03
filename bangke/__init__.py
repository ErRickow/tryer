import os
import platform
import subprocess
from importlib import metadata
from bangke.others import Colors
from config import Configuration

class Config:
    """This class generates the configs."""
    pass

def is_local_host():
    """Check if it is localhost by checking the existence of config.txt."""
    return os.path.exists("config.txt")

class Tools:
    """Use it for installing the required packages."""
    device = platform.uname().system.lower()
    is_linux = device == "linux"

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system("clear" if self.is_linux else "cls")

    def read_config_file(self):
        """Read configuration from config.txt."""
        if not os.path.isfile("config.txt"):
            print("config.txt file doesn't exist, exiting...")
            exit(0)

        with open("config.txt") as f:
            return [line.strip() for line in f if line.strip()]

    def setup_config(self):
        """Setup configuration values from config.txt and Configuration class."""
        content = self.read_config_file()
        
        print(Colors.block + "Setting configuration values.\n\n" + Colors.reset)
        count = 1

        for line in content:
            key_value = line.split("=")
            if len(key_value) < 2:
                print(f"Skipping invalid configuration line: {line}")
                continue

            key, value = key_value[0].strip(), key_value[1].strip()
            setattr(Config, key, int(value) if value.isdigit() else value)
            print(f"[{count}] Added config = {key} with value = {value}\n")
            count += 1

        self.set_remaining_config(count)

    def set_remaining_config(self, count):
        """Set remaining configuration values from Configuration class."""
        print(Colors.block + "\nSetting remaining configuration values\n\n" + Colors.reset)
        for attr in dir(Configuration):
            if attr.isupper() and not hasattr(Config, attr):
                value = getattr(Configuration, attr)
                setattr(Config, attr, value)
                print(f"[{count}] Added config = {attr} with value = {value}\n")
                count += 1

# Initialize Tools and setup configuration
tools = Tools()

if is_local_host():
    tools.setup_config()
else:
    print("Setting the Non-LocalHost setup ... !")
    for attr in dir(Configuration):
        if attr.isupper() and not hasattr(Config, attr):
            setattr(Config, attr, getattr(Configuration, attr))

# Default import
from bangke.ubot import app
bot = app.bot
from bangke.core.filters import gen