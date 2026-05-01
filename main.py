import flet as ft

def main(page: ft.Page):
    # Esta es una prueba simple para ver si la app abre
    page.add(
        ft.Column([
            ft.Text("¡Élite Travel!", size=30, weight="bold"),
            ft.Text("Si puedes leer esto, el sistema funciona."),
            ft.Text("El problema anterior era la ruta de la imagen."),
            ft.Icon(ft.Icons.CHECK_CIRCLE, color="green", size=50)
        ], horizontal_alignment="center")
    )

if __name__ == "__main__":
    # Dejamos assets_dir para que no de error si la carpeta existe
    ft.app(target=main, assets_dir="assets")
