# import flet as ft
# import webbrowser
# import os
#
# def main(page: ft.Page):
#     page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
#
#     def button_clicked(e):
#         page.add(ft.Text("Clicked!"))
#         os.startfile(r'C:\Code\pythonProject1\queue orders.py')
#
#     def button_clicked1(e):
#         page.add(ft.Text("Clicked!"))
#         webbrowser.open("https://youtu.be/amXl7FG7J4c?si=HvY3h-S8cSlGB3a_")
#
#     page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
#     page.add(ft.ElevatedButton(text="Yoooo Im adama Rose", on_click=button_clicked1))
#
# ft.app(target=main)



import flet as ft
import requests

def main(page: ft.Page):
    # Загрузка содержимого роадмапа из удаленного файла на GitHub
    url = "https://raw.githubusercontent.com/ILIakkk/ILIakkk/main/roadmap.txt"
    response = requests.get(url)
    roadmap_text = response.text

    # Функция для копирования текста роадмапа в буфер обмена
    def copy_roadmap(e):
        page.set_clipboard(roadmap_text)
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Роадмап скопирован в буфер обмена!"),
            action="Закрыть",
        )
        page.snack_bar.open = True
        page.update()

    # Создание интерфейса приложения
    page.title = "Мой роадмап"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False

    # Создание кнопки копирования
    copy_button = ft.IconButton(
        icon=ft.icons.COPY,
        tooltip="Копировать роадмап",
        on_click=copy_roadmap,
    )

    # Создание контейнера для отображения роадмапа
    roadmap_container = ft.Container(
        content=ft.Markdown(
            value=roadmap_text,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        ),
        border_radius=10,
        padding=20,
        expand=True,
        ink=True,
        on_hover=lambda _: page.update(),
    )

    # Добавление элементов на страницу
    page.add(
        ft.Row(
            [
                ft.Text(
                    "Мой роадмап",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(expand=True),
                copy_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Divider(height=4, color=ft.colors.BLACK26),
        roadmap_container,
    )

ft.app(target=main)