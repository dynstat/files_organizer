import flet as ft
from flet.buttons import RoundedRectangleBorder
from flet.border import BorderSide


button_style1 = ft.ButtonStyle(
    overlay_color=ft.colors.TRANSPARENT,
    shape={
        ft.MaterialState.HOVERED.value: RoundedRectangleBorder(radius=10),
        ft.MaterialState.DEFAULT.value: RoundedRectangleBorder(radius=40),
    },
    bgcolor={
        ft.MaterialState.HOVERED.value: ft.colors.BLUE_50,
        ft.MaterialState.DEFAULT.value: ft.colors.WHITE,
    },
    color={ft.MaterialState.DEFAULT.value: ft.colors.BLACK},
    side=BorderSide(color=ft.colors.BLACK, width=1),
)
