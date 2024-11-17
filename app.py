import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///banco.db"
engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main( page: ft.Page ):
    page.title = "Cadastro App"

    def cadastrar(e):
        novo_produto = Produto( produto=produto.value, preco=preco.value )
        session.add(novo_produto)
        session.commit()
        print('Produto salvo com sucesso.')
    
    txt_titulo = ft.Text('Titulo do produto')
    
    produto = ft.TextField(label="Digite o titulo do produto...", 
    text_align=ft.TextAlign.LEFT)

    preco = ft.TextField(label="R$ 0,00", 
    text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_titulo,
        produto,
        preco, 
        btn_produto
    )

ft.app( target=main )

