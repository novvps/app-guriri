import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#ffffff'
    page.title = "Guriri App"
    page.horizontal_alignment = "center"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(ft.Text(value="Guriri", size=80, weight="bold", color="#000000"))
    page.add(ft.Text(value="Explore esse paraíso", size=30, weight="bold", color="#000000"))

ft.app(main)