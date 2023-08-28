# starting point of the app
import os
import shutil
from pathlib import Path
from time import sleep
from files_organizer.globals_ import globals_init

import flet as ft  # importing flet
import gui.main_gui_ as gui  # gui module contianing functions, views


# main
if __name__ == "__main__":
    globals_init()
    ft.app(target=gui.main)  # calling the function of the flet library to start the gui
