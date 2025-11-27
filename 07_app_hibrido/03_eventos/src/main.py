import flet as ft


def main(page: ft.Page):
    # função do evento
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()

    # propriedades da página
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # declaração de váriaveis
    nome = ft.TextField(label="Informe seu nome", on_submit=exibir_nome)
    nome_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=35, weight="bold"), # weight="bold" = deixar o texto em negrito. size=35 = Tamanho do texto.
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
            nome,
            ft.ElevatedButton("Aperta aí meu chegado", on_click=exibir_nome),
            nome_saida,

        
        
    )


ft.app(main)


"""Indique qual é o melhor combustivel (mais vantajoso) para um carro flet

etanol tem que estar a 70% do valor da gasolina para estar vanjoso"""