from views.view import View, ViewsInitialStates
import utils.services as services
from components.component import Component, DefaultComponents
from utils.enums import FletNames, Colors
import flet as ft

header_size = 27
text_size = header_size - 10
cont_bg_color = '#122EC4B6'

cont_options = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text('Opcje', size=header_size),
            ft.Column(
                [
                    ft.Row(
                        controls=[
                            ft.Container(
                                ft.Text('Ciemny motyw', size=text_size),
                                padding=ft.Padding(top=0, left=10, right=0, bottom=0),
                            ),
                            ft.Container(ft.Switch()),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                ft.Text('Język', size=text_size),
                                padding=ft.Padding(top=0, left=10, right=0, bottom=0),
                            ),
                            ft.Dropdown(
                                options=[
                                    ft.dropdown.Option('Polski'),
                                    ft.dropdown.Option('English'),
                                ],
                                width=150,
                                height=61,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                ],
                spacing=0,
            )
        ],
    ),
    bgcolor=cont_bg_color,
    margin=10,
    padding=10,
    border_radius=10,
)

cont_account = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text('Konto', size=header_size),
            ft.Row([ft.TextButton(
                content=ft.Text('Zmień hasło', color='#22978C', size=text_size),
            )]),
            ft.Row([ft.TextButton(
                content=ft.Text('Usuń konto', color='#22978C', size=text_size),
            )]),
        ],
        spacing=0,
    ),
    bgcolor=cont_bg_color,
    margin=10,
    padding=10,
    border_radius=10,
)

cont_misc = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(value='Inne', size=header_size),
            ft.Row([ft.TextButton(
                content=ft.Text(value='Zgłoś błąd', color='#22978C', size=text_size),
            )]),
            ft.Row(
                controls=[
                    ft.Container(
                        ft.Text(value='Wersja aplikacji:', size=text_size),
                        padding=ft.Padding(top=0, left=10, right=0, bottom=0)
                    ),
                    ft.Container(ft.Text(value='1.0.0', size=text_size)),
                ],
                spacing=20
            ),
        ],
        spacing=0,
    ),
    bgcolor=cont_bg_color,
    margin=10,
    padding=10,
    border_radius=10,
)

settings = View(name=FletNames.SETTINGS, route=f"/{FletNames.SETTINGS}")
settings.add_component(
    Component(
        content=[
            ft.AppBar(
                title=ft.Text("Ustawienia aplikacji"),
                bgcolor=Colors.PRIMARY_DARKER
            )
        ],
        description="App bar showing the title of the page and allowing to navigate back to the home page.")
)
settings.add_component(
    Component(
        content=[
            ft.Column(
                [
                    cont_options,
                    cont_account,
                    cont_misc,
                ],
                scroll=ft.ScrollMode.HIDDEN,
                expand=True,
            )
        ],
        description="Settings page content."
    )
)
ViewsInitialStates.set_settings_copy(settings)
settings.log()
