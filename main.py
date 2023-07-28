import flet as ft
import requests
import json
from modules import api

def main(page):
    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    greetings = ft.Column()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def btn_click(e):
        parse_json = api.data
        matches = [c for c in parse_json if username.value == c['name'] and password.value == c['password']]
        if matches:
            go_login(e)
        else:
            page.controls.append(ft.Text("GAGAL LOGIN!"))
        username.value = ""
        password.value = ""
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Login"),center_title=True, bgcolor=ft.colors.SURFACE_VARIANT),
                    username,
                    password,
                    ft.Container(alignment=ft.alignment.center, content=ft.ElevatedButton("Login", on_click=btn_click)),
                    greetings,
                ],
            )
        )
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.AppBar(title=ft.Text("login"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def go_login(e):
        page.route = "/login"
        page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)