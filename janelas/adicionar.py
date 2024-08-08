import flet as ft
from querys.inserts import INSERT_DIVIDAS
from conexao import Conexao

class AdicionarDivida(ft.UserControl):
    def __init__(self, conexao):  # Recebe a conexão do banco de dados
        super().__init__()
        self.conexao = conexao

    def build(self):
        self.nome_input = ft.TextField(label="Nome")
        self.valor_input = ft.TextField(label="Valor")
        self.prazo_input = ft.DatePicker(on_change=self.date_picker_change)

        btn_salvar = ft.ElevatedButton(text="Salvar", on_click=self.salvar_divida)

        return ft.Column(
            [
                self.nome_input,
                self.valor_input,
                self.prazo_input,
                btn_salvar,
            ],
            width=300,
            height=300,
        )

    def salvar_divida(self, e):
        nome = self.nome_input.value
        valor = float(self.valor_input.value)
        prazo = self.prazo_input.value.strftime("%Y-%m-%d")

        with self.conexao as conn:
            conn.executar_query(INSERT_DIVIDAS, (nome, valor, prazo))

        self.page.dialog(ft.AlertDialog(title="Sucesso", content="Dívida adicionada com sucesso!")).open()
        
    def date_picker_change(self, e):
        self.prazo = e.control.value

def main(page: ft.Page):
    conexao = Conexao("controle_dividas", "postgres", "cicada3301")
    page.title = "Adicionar Dívida"
    page.add(AdicionarDivida(conexao))
ft.app(target=main)
