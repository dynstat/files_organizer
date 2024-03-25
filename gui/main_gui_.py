import flet as ft

# personal imports
from .app_styles import button_style1


from files_organizer import (
    afo,
)  # imported the modulw which has all the functions related to moving, copying, resetting etc

from files_organizer import globals_  # globals import


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
            "FILES ORGANIZER", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD, size=35
        ),
        center_title=True,
        bgcolor=ft.colors.WHITE70,
    )
    # Control 0 Ends here

    # Control 1.1 Starts here
    target_dir_row = ft.Container(
        ft.Row(
            controls=[
                ft.Container(
                    ft.Text("Folder to organize:", size=20),
                    padding=ft.padding.only(left=10),
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
                            ft.Text("Destination folder:", size=20),
                            padding=ft.padding.only(left=10),
                            alignment=ft.alignment.center_left,
                            # bgcolor=ft.colors.AMBER_100,
                        ),
                        ft.Container(
                            ft.TextField(
                                hint_text="same as source",
                                border_radius=15,
                                height=50,
                                text_align=ft.TextAlign.LEFT,
                                border_width=1,
                                text_style=ft.TextStyle(color=ft.colors.BLACK87),
                                # expand=True,
                            ),
                            # bgcolor=ft.colors.AMBER_300,
                            expand=True,
                            padding=ft.Padding(left=0, right=0, top=0, bottom=0),
                            width=500,
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Browse",
                                style=button_style1,
                                on_click=lambda _: pick_folder_dialog2.get_directory_path(),
                            ),
                            # bgcolor=ft.colors.AMBER_100,
                            padding=10,
                        ),
                    ]
                )
            ],
        ),
        # bgcolor=ft.colors.AMBER_200,
    )
    # Control 1.2 End

    path_ctrl = target_dir_row.content.controls[1].content
    path_ctrl2 = group_outer_col.content.controls[0].controls[1].content

    def wrapper_organize(cntrl):
        try:
            if cntrl.control.text == "STOP":
                cntrl.control.text = "ORGANIZE"

                globals_.KEEP_RUNNING = 0
                cntrl.control.update()
                #! yet to implement keep-running and stopping mechanism
                return
            if path_ctrl.hint_text == "path to the folder" or path_ctrl.hint_text == "":
                print("choose folder")
            else:
                if (
                    path_ctrl2.hint_text == "same as source"
                    or path_ctrl2.hint_text == ""
                ):
                    print("Organizing...")
                    afo.organize_folder(path_ctrl.hint_text)
                    print("Organized")

            #! To be used while implementing keep-running and stopping mechanism
            # if cntrl.control.text == "ORGANIZE":
            #     cntrl.control.text = "STOP"
            # elif cntrl.control.text == "STOP":
            #     cntrl.control.text = "ORGANIZE"

        except Exception as e:
            print(f"error in wrapper_organize: {e}")
            cntrl.control.text == "ERROR"
        cntrl.control.update()

    def wrapper_deorg(cntrl):
        print("DE-Organizing...")
        try:
            if cntrl.control.text != "DE-ORGANIZE":
                # cntrl.control.text = "ORGANIZE"

                # globals_.KEEP_RUNNING = 0
                # cntrl.control.update()
                #! yet to implement keep-running and stopping mechanism
                return
            if path_ctrl.hint_text == "path to the folder" or path_ctrl.hint_text == "":
                print("choose folder")
            else:
                if (
                    path_ctrl2.hint_text == "same as source"
                    or path_ctrl2.hint_text == ""
                ):
                    print("DE - Organizing...")
                    afo.de_organize(path_ctrl.hint_text)
                    print("DE-Organized")

        except Exception as e:
            print(f"error in wrapper_deorg: {e}")
            cntrl.control.text == "ERROR"
        cntrl.control.update()

    start_btn = ft.ElevatedButton(
        text="ORGANIZE",
        style=button_style1,
        on_click=lambda c: wrapper_organize(c),
    )
    Deorg_btn = ft.ElevatedButton(
        text="DE-ORGANIZE",
        style=button_style1,
        on_click=lambda c: wrapper_deorg(c),
    )

    # Control 1 Starts
    main_col = ft.Column(controls=[target_dir_row, group_outer_col])
    # Control 1 End

    # file picker for target folder.
    def pick_folder_result(e: ft.FilePickerResultEvent):
        nonlocal path_ctrl
        print(f"folder path selected, {e.path} ")
        path_ctrl.hint_text = e.path
        path_ctrl.update()

    # file picker for the destination folder.
    def pick_folder_result2(e: ft.FilePickerResultEvent):
        nonlocal path_ctrl2
        print(f"folder path selected, {e.path} ")
        path_ctrl2.hint_text = e.path
        path_ctrl2.update()

    pick_folder_dialog = ft.FilePicker(on_result=pick_folder_result)
    pick_folder_dialog2 = ft.FilePicker(on_result=pick_folder_result2)

    page.overlay.append(pick_folder_dialog)
    page.overlay.append(pick_folder_dialog2)

    page.controls.append(title_appBar)
    page.controls.append(ft.Divider(thickness=1, opacity=0, height=10))
    page.controls.append(main_col)
    page.controls.append(start_btn)
    page.controls.append(Deorg_btn)

    page.update()


# Not the actual entry point, just for testing.
if __name__ == "__main__":
    ft.app(target=main)
