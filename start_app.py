# starting point of the app


import flet as ft  # importing flet
import gui.main_gui_ as gui  # gui module contianing functions, views


# main
if __name__ == "__main__":
    ft.app(target=gui.main)  # calling the function of the flet library to start the gui
