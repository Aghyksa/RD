import flet as ft

def create_username_field():
    return ft.Container(
        content=ft.TextField(label="Username", autofocus=True),
        padding=5,
        width=500,
        height=100,
    )

def create_password_field():
    return ft.Container(
        content=ft.TextField(label="Password", password=True, can_reveal_password=True),
        padding=5,
        width=500,
        height=100,
    )

def create_app_bar():
    return ft.AppBar(title=ft.Text("Home"), center_title=True, bgcolor=ft.colors.SURFACE_VARIANT)

def create_greetings_column():
    return ft.Column()
