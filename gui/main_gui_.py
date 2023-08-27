import flet as ft

# personal imports
from .app_styles import button_style1


from files_organizer import (
    afo,
)  # imported the modulw which has all the functions related to moving, copying, resetting etc


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_height = 540
    page.window_width = 686
    page.padding = 0
    page.window_min_width = 680
    # page.window_title_bar_hidden = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Control 0 Start
    title_appBar = ft.AppBar(
        title=ft.Text(
            "FILES ORGANIZER", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD
        ),
        center_title=True,
        bgcolor=ft.colors.BLUE_100,
    )
    # Control 0 Ends here

    # Control 1.1 Starts here
    target_dir_row = ft.Container(
        ft.Row(
            controls=[
                ft.Container(
                    ft.Text("Folder to organize:", size=20),
                    padding=0,
                    alignment=ft.alignment.center_left,
                    # bgcolor=ft.colors.AMBER_100,
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
                        on_click=lambda _: pick_folder_dialog.get_directory_path(),
                    ),
                    # bgcolor=ft.colors.AMBER_100,
                    padding=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=1,
        # bgcolor=ft.colors.RED_50,
    )
    # Control 1.1 End

    # Control 1.2 Start
    group_outer_col = ft.Container(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            ft.Text("New Folder Name:", size=20),
                            padding=0,
                            alignment=ft.alignment.center_left,
                            # bgcolor=ft.colors.AMBER_100,
                        ),
                        ft.Container(
                            ft.TextField(
                                hint_text="organized_folder",
                                border_radius=15,
                                height=50,
                                text_align=ft.TextAlign.LEFT,
                                border_width=1,
                                text_style=ft.TextStyle(color=ft.colors.BLACK87),
                                # expand=True,
                            ),
                            # bgcolor=ft.colors.AMBER_300,
                            expand=True,
                            padding=ft.Padding(left=0, right=125, top=0, bottom=0),
                            width=500,
                        ),
                    ]
                )
            ],
        ),
        # bgcolor=ft.colors.AMBER_200,
    )
    # Control 1.2 End

    path_ctrl = target_dir_row.content.controls[1].content

    def wrapper():
        if path_ctrl.hint_text == "path to the folder":
            print("choose folder")
        else:
            print("Organizing...")
            afo.organize_files(path_ctrl.hint_text)
            print("Organized")

    start_btn = ft.ElevatedButton(
        text="ORGANIZE",
        style=button_style1,
        on_click=lambda _: wrapper(),
    )

    # Control 1 Starts
    main_col = ft.Column(controls=[target_dir_row, group_outer_col])
    # Control 1 End

    def pick_folder_result(e: ft.FilePickerResultEvent):
        nonlocal path_ctrl
        print(f"folder path selected, {e.path} ")
        path_ctrl.hint_text = e.path
        path_ctrl.update()

    pick_folder_dialog = ft.FilePicker(on_result=pick_folder_result)

    page.overlay.append(pick_folder_dialog)

    page.controls.append(title_appBar)
    page.controls.append(ft.Divider(thickness=1, opacity=0, height=10))
    page.controls.append(main_col)
    page.controls.append(start_btn)

    page.update()


# Not the actual entry point, just for testing.
if __name__ == "__main__":
    ft.app(target=main)
