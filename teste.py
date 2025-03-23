import flet as ft
import flet.map as map


def main(page: ft.Page):
    # Coordenadas da Ilha de Guriri, São Mateus, ES
    ilha_guriri_lat = -18.7203
    ilha_guriri_lon = -39.8997

    # Adicionando o mapa com a visualização focada na Ilha de Guriri
    page.add(
        ft.Text("Visualização do Mapa - Ilha de Guriri"),
        map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(ilha_guriri_lat, ilha_guriri_lon),  # Focando na Ilha de Guriri
            initial_zoom=12,  # Zoom adequado para visualizar a ilha
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            layers=[
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    on_image_error=lambda e: print("Erro no TileLayer"),
                ),
                map.SimpleAttribution(
                    text="Flet",
                    alignment=ft.alignment.top_right,
                    on_click=lambda e: print("Clique na atribuição Flet"),
                ),
                map.MarkerLayer(
                    markers=[
                        map.Marker(
                            content=ft.Icon(ft.Icons.LOCATION_ON),
                            coordinates=map.MapLatitudeLongitude(ilha_guriri_lat, ilha_guriri_lon),
                        ),
                    ],
                ),
            ],
        ),
    )


ft.app(main)
