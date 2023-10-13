# import flet as ft
# import sys 
# sys.path.append('/Users/lyon/Desktop/Lyon/RD')
# from modules import api


        
# def main(page):
#     parse_json = api.data
#     items = []


#     for data in parse_json:
#         name = data['name'] 
#         password = data['password']
#         items.append(
#             ft.Container(
#                 alignment=ft.alignment.center,
#                 content=ft.TextButton(
#                     text=name,
#                 ),
#             )
#         )
        
#     page.views.append(
#         ft.View(
#         "/user",
#             [
#             ft.AppBar(title=ft.Text("User"),center_title=True, bgcolor=ft.colors.SURFACE_VARIANT),
#             *items
#             ]
#         ),
#     ),
#     page.update()

# ft.app(target=main)
