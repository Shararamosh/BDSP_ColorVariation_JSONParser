"""
    Script containing general functions.
"""
import os
import sys
import logging
from tkinter import Tk
from PIL.ImageTk import PhotoImage
from rich.logging import RichHandler
from rich.console import Console

RICH_CONSOLE = Console()


def get_resource_path(file_path: str) -> str:
    """
    Returns path to file or directory inside project, when used PyInstaller or Nuitka are used.
    :param file_path: Original path to file or directory.
    :return: Modified path to file or directory.
    """
    if "NUITKA_ONEFILE_PARENT" in os.environ:
        base_path = os.path.dirname(sys.executable)
    elif hasattr(sys, "_MEIPASS"):
        base_path = getattr(sys, "_MEIPASS")
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, file_path)


def init_app(icon_path: str):
    """
    Initiating app for launch.
    :param icon_path: Path to icon file.
    """
    sys.tracebacklimit = 0
    logging.basicConfig(format="%(message)s", level=logging.INFO, handlers=[
        RichHandler(level=logging.INFO, console=RICH_CONSOLE, rich_tracebacks=True)])
    root = Tk()
    root.withdraw()
    root.iconphoto(True, PhotoImage(file=get_resource_path(icon_path)))
