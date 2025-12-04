import sqlite3
import pandas as pd
from tabulate import tabulate

conexao = sqlite3.connect('banco.db')

class Banco():
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def criacao_Banco(self):
        global conexao
        conexao.execute(
            '''CREATE TABLE IF NOT EXISTS Cadastro (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, IDADE INTEGER)''')
        conexao.commit()
        print('\nTabela criada com êxito !\n')

    def get_Valores(self):
        self.criacao_Banco()
        try:
            dados = pd.read_sql_query("SELECT * FROM Cadastro", conexao)
            print("\n=== RELATÓRIO DE CADASTRO ===")
            print(tabulate(dados, headers='keys', tablefmt='grid', showindex=False))


        except ValueError:
            print("\nOcorreu um Erro ao Consultar o Banco de Dados!")

    def set_Cadastro(self, nome, idade):
        self.criacao_Banco()
        self.nome = nome
        self.idade = idade

        try:
            conexao.execute(f"INSERT INTO Cadastro (nome, idade) VALUES (?, ?)",
                            (str(self.nome), int(self.idade)))
            conexao.commit()
            print("Cadastrado com Sucesso")

        except ValueError:
            print('\nErro ao salvar no Banco')

    def set_update(self, nome, idade, id):
        self.criacao_Banco()
        try:
            cursor = conexao.cursor()
            cursor.execute(f"UPDATE Cadastro SET NOME = ?, IDADE = ? WHERE ID = ?", (nome, idade, id))
            conexao.commit()
            cursor.close()
            print("\nAtualizado com sucesso")

        except:
            print("\nErro ao Atualizar")

    def set_excluir(self, id):
        self.criacao_Banco()
        self.get_Valores()
        confirmar = input('\nDeseja Excluir ? Sim/Nao: ').lower()

        if confirmar == "sim" or confirmar == "s" or confirmar == "yes":
            conexao.execute(f"DELETE FROM Cadastro WHERE ID = ?", [id])
            conexao.commit()
            print('\nExcluido com Sucesso !')

        else:
            pass

    def sair(self):
        conexao.close()
        print('\n\nAté a proxima | Conexão DB encerrada\n')
        exit()