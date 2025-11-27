import flet as ft


def main(page: ft.Page):

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Minha primeira aplicação.", size=30, weight="bold", color="yelow", font_family="Garamond"),
                alignment=ft.alignment.center,
            )
        ),
        ft.Container(
            ft.Image(
                src="1.jpg",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Não foi possível carregar a imagem."),
                width=800,
                height=600
            ),
            alignment=ft.alignment.center,
            expand=True #Esse comando serve para centralizar a imagem no centro da janela, tanto verticalmente quanto orizontalmente.
        )
    )


ft.app(main)