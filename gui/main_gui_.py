import flet as ft
from flet.buttons import RoundedRectangleBorder
from flet.border import BorderSide


# personal imports
from app_styles import button_style1


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_height = 540
    page.window_width = 686
    page.padding = 0
    # page.window_title_bar_hidden = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Control 0 Start
    title_appBar = ft.AppBar(
        title=ft.Text("FILES ORGANIZER", color=ft.colors.BLUE),
        center_title=True,
        bgcolor=ft.colors.BLUE_100,
    )
    # Control 0 End

    # Control 1.1 Start
    target_dir_row = ft.Container(
        ft.Row(
            controls=[
                ft.Container(
                    ft.Text("Folder to organize:", size=20),
                    padding=0,
                    alignment=ft.alignment.center_left,
                    bgcolor=ft.colors.AMBER_100,
                ),
                ft.Container(
                    ft.TextField(
                        hint_text="path to the folder",
                        border_radius=15,
                        height=50,
                        text_align=ft.TextAlign.LEFT,
                        border_width=1,
                        text_style=ft.TextStyle(color=ft.colors.BLACK12),
                        # expand=True,
                    ),
                    # bgcolor=ft.colors.AMBER_300,
                    expand=True,
                    padding=10,
                ),
                ft.Container(
                    ft.ElevatedButton(
                        text="Browse",
                        style=button_style1,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),
                    bgcolor=ft.colors.AMBER_100,
                    padding=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=1,
        bgcolor=ft.colors.RED_50,
    )
    # Control 1.1 End

    # Control 1.2 Start
    group_outer_col = ft.Container(
        ft.Column(
            controls=[],
        ),
        bgcolor=ft.colors.AMBER_200,
    )
    # Control 1.2 End

    # Control 1 Starts
    main_col = ft.Column(controls=[target_dir_row, group_outer_col])
    # Control 1 End

    def pick_files_result(e: ft.FilePickerResultEvent):
        print("file picker started")

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)

    page.controls.append(title_appBar)
    page.controls.append(ft.Divider(thickness=10, opacity=0))
    page.controls.append(main_col)

    page.update()


ft.app(target=main)
