from PyQt5.QtWidgets import QApplication, QWidget,QDialog, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from conexao import Conexao
from janelas.adicionar import AdicionarDivida
from querys.selects import SELECT_DIVIDAS

class Interface(QWidget):
    def __init__(self):
        super().__init__()

        self.conexao = Conexao("controle_dividas", "postgres", "cicada3301")  # Dados de conexão

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        btn_adicionar = QPushButton("Adicionar")
        btn_adicionar.clicked.connect(self.abrir_janela_adicionar)
        
        btn_editar = QPushButton("Visualizar em Dashboard")
        btn_remover = QPushButton("Remover")
        layout.addWidget(btn_adicionar)
        layout.addWidget(btn_editar)
        layout.addWidget(btn_remover)

        self.tabela = QTableWidget()
        self.atualizar_tabela()  # Preenche a tabela inicialmente
        layout.addWidget(self.tabela)

        self.setLayout(layout)

    def abrir_janela_adicionar(self):
        janela_adicionar = AdicionarDivida(self.conexao)
        if janela_adicionar.exec_() == QDialog.Accepted:  # Se a janela for fechada com "Salvar"
            self.atualizar_tabela() 
            
    def atualizar_tabela(self):
        # Obter dívidas e nomes das colunas dentro do mesmo bloco with
        with self.conexao as conn:
            dividas = conn.executar_query(SELECT_DIVIDAS)
            conn.cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'dividas'")
            nomes_colunas = [coluna[0] for coluna in conn.cursor.fetchall()]

        # Atualizar a tabela fora do bloco with
        self.tabela.setRowCount(len(dividas))
        self.tabela.setColumnCount(len(dividas[0]))  # Assume que todas as linhas têm o mesmo número de colunas
        self.tabela.setHorizontalHeaderLabels(nomes_colunas)  # Definir cabeçalho da tabela

        for i, linha in enumerate(dividas):
            for j, valor in enumerate(linha):
                item = QTableWidgetItem(str(valor))  # Converter valor para string
                self.tabela.setItem(i, j, item)
if __name__ == "__main__":
    app = QApplication([])
    interface = Interface()
    interface.show()
    app.exec_()
