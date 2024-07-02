import psycopg2

class Conexao:
    def __init__(self, dbname="controle_dividas", user="postgres", password="cicada3301", host="localhost", port=5432):
        try:
            self.conn = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Erro na conexão com o banco de dados: {e}")
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def executar_query(self, query, parametros=None):
        self.cursor.execute(query, parametros)
        self.conn.commit()
        return self.cursor.fetchall()
