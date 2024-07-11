from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QDateTimeEdit
from querys.inserts import INSERT_DIVIDAS
from conexao import Conexao

class AdicionarDivida(QDialog):
    def __init__(self, conexao):  # Recebe a conexão do banco de dados
        super().__init__()
        self.conexao = conexao
        self.setWindowTitle("Adicionar Dívida")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.nome_input = QLineEdit()
        form_layout.addRow("Nome:", self.nome_input)

        self.valor_input = QLineEdit()
        form_layout.addRow("Valor:", self.valor_input)

        self.prazo_input = QDateTimeEdit()
        self.prazo_input.setCalendarPopup(True)  # Mostrar calendário pop-up
        form_layout.addRow("Prazo:", self.prazo_input)

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(self.salvar_divida)
        layout.addLayout(form_layout)
        layout.addWidget(btn_salvar)

        self.setLayout(layout)

    def salvar_divida(self):
        nome = self.input_nome.text()
        valor = self.input_valor.float()
        prazo = self.prazo_input.dateTime().toString("yyyy-MM-dd")  


        with self.conexao as conn:
            conn.executar_query(INSERT_DIVIDAS, (nome, valor, prazo))  

        self.accept()  