import flet as ft
from conexao import Conexao
from querys.selects import SELECT_DIVIDAS

class Interface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Gerenciador de Dívidas"
        
        # Inicializa a conexão com o banco de dados
        self.conexao = Conexao(dbname="controle_dividas", user="postgres", password="cicada3301", host="localhost", port="5432") 
        
        self.data_table = None 
        self.criar_interface()

    def criar_interface(self):
        self.page.add(
            ft.Row([
                ft.ElevatedButton("Adicionar", on_click=self.adicionar),
                ft.ElevatedButton("Visualizar Dashboard", on_click=self.dashboard),
                ft.ElevatedButton("Editar", on_click=self.editar),
                ft.ElevatedButton("Remover", on_click=self.remover)
            ])
        )
        self.carregar_dados()

    def carregar_dados(self):
        dados = self.conexao.executar_query(SELECT_DIVIDAS)
        
        if dados: 
            colunas = [
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Prazo")),
            ]
            
            # Cria as linhas da tabela com base nos dados retornados
            linhas = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(linha[0]))),  # ID
                    ft.DataCell(ft.Text(str(linha[1]))),  # Nome
                    ft.DataCell(ft.Text(str(linha[2]))),  # Valor
                    ft.DataCell(ft.Text(str(linha[3])))   # Prazo
                ]) for linha in dados
            ]
            
            self.data_table = ft.DataTable(columns=colunas, rows=linhas)
            self.page.add(self.data_table) 
        else:
            self.page.add(ft.Text("Nenhum dado encontrado.")) 

        self.page.update()

    def adicionar(self, e):
        # Implemente a lógica para adicionar uma nova dívida
        pass

    def dashboard(self, e):
        # Implemente a lógica para visualizar o dashboard
        pass

    def editar(self, e):
        # Implemente a lógica para editar uma dívida
        pass

    def remover(self, e):
        # Implemente a lógica para remover uma dívida
        pass

if __name__ == "__main__":
    ft.app(target=Interface)