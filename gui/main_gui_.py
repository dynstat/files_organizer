import flet as ft


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_height = 540
    page.window_width = 886
    page.padding = 0
    # page.window_title_bar_hidden = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Control 0 Start
    title_appBar = ft.AppBar(
        title=ft.Text("FILES ORGANIZER"),
        center_title=True,
        bgcolor=ft.colors.TRANSPARENT,
    )
    # Control 0 End

    # Control 1.1 Start
    target_dir_row = ft.Row(controls=[ft.Text("Target Folder:")])
    # Control 1.1 End

    # Control 1.2 Start
    group_outer_col = ft.Column(controls=[group_inner_col, add_more_group_row])
    # Control 1.2 End

    # Control 1 Starts
    main_col = ft.Column(controls=[target_dir_row, group_outer_col])
    # Control 1 End

    page.controls.append(title_appBar)
    page.update()


ft.app(target=main)
