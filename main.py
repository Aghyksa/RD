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
            greetings.controls.append(ft.Text("GAGAL LOGIN!"))
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
                    ft.AppBar(title=ft.Text("Home"),center_title=True, bgcolor=ft.colors.SURFACE_VARIANT),
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
                        ft.AppBar(title=ft.Text("Home"), center_title=True, bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.NavigationBar(
                            destinations=[
                                ft.NavigationDestination(icon=ft.icons.EXPLORE,selected_icon=ft.icons.EXPLORE_OUTLINED, label="Explore"),
                                ft.NavigationDestination(icon=ft.icons.SEARCH,selected_icon=ft.icons.SEARCH_ROUNDED, label="Search"),
                                ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Boomark")
                            ],
                            on_change=lambda e: define_route(e),
                            
                        ),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/"))
                    ]
                )
            )
        elif page.route == "/user":
            page.views.append(
                ft.View(
                    "/user",
                    [
                        ft.AppBar(title=ft.Text("User"), center_title=True, bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home on user", on_click=lambda _: page.go("/")),
                        
                    ]
                )
            )
        page.update()

    def define_route(e):
        if page.route == "/login":
            if e.data == '1':
                page.route = "/user"
                route_change(e)


    def go_login(e):
        page.route = "/login"
        page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)