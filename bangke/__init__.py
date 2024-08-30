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
