import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.window.height = "auto"
        page.update()

    new_task = ft.TextField(hint_text="شنو سويت اليوم?")

    page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))

ft.app(main)
