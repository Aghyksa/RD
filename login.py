import flet as ft
from modules import api
from components.field import create_username_field, create_password_field, create_app_bar, create_greetings_column


def main(page):
    username = create_username_field()
    password = create_password_field()
    app_bar = create_app_bar()
    greetings = create_greetings_column()

    def button_login(e):
            parse_json = api.data
            matches = [c for c in parse_json if username.content.value == c['name'] and password.content.value == c['password']]
            if matches:
                greetings.controls.append(ft.Text("BERHASIL LOGIN!"))
            else:
                greetings.controls.append(ft.Text("GAGAL LOGIN!"))
            username.value = ""
            password.value = ""
            page.update()

    page.add(
        app_bar,
        ft.Container(alignment=ft.alignment.center, content=username),
        ft.Container(alignment=ft.alignment.center, content=password),
        ft.Container(alignment=ft.alignment.center, content=ft.ElevatedButton("Login",on_click=button_login,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))),
        greetings,
    )

ft.app(target=main)
