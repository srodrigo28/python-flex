import flet as ft

def main( page: ft.Page ):
    page.title = "Cadastro App"
    
    txt_titulo = ft.Text('Titulo do produto')
    
    produto = ft.TextField(label="Digite o titulo do produto...", 
    text_align=ft.TextAlign.LEFT)

    preco = ft.TextField(label="R$ 0,00", 
    text_align=ft.TextAlign.LEFT)

    page.add(
        txt_titulo,
        produto,
        preco
    )

ft.app( target=main )

