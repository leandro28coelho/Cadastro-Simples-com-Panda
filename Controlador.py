import sqlite3
import pandas as pd

conexao = sqlite3.connect('banco.db')

class Banco():
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        global conexao

    def criacao_Banco(self):
        conexao.execute(
            '''CREATE TABLE IF NOT EXISTS Cadastro (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, IDADE INTEGER)''')

    def get_Valores(self):
        try:
            dados = pd.read_sql_query("SELECT * FROM Cadastro", conexao)
            consulta = dados.to_string(index=False)
            print('\n\tREGISTROS')
            print(22*'_')
            print(consulta)
            print(23 *'_')

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
            print("\nCadastrado com Sucesso")

        except ValueError:
            print('\nErro ao salvar no Banco')

    def set_update(self, nome, idade, id):
        try:
            cursor = conexao.cursor()
            cursor.execute(f"UPDATE Cadastro SET NOME = ?, IDADE = ? WHERE ID = ?", (nome, idade, id))
            conexao.commit()
            cursor.close()
            print("\nAtualizado com sucesso")

        except:
            print("\nErro ao Atualizar")

    def set_excluir(self, id):
        dados = pd.read_sql_query(f"SELECT * FROM Cadastro WHERE ID = {(id)}", conexao)
        consulta = dados.to_string(index=False)
        print(22*'_')
        print(consulta)
        print(23*'_')
        confirmar = input('Deseja Excluir ? Sim/Nao: ')
        confirmar = confirmar.lower()

        if confirmar == "sim" or confirmar == "s" or confirmar == "yes":
            conexao.execute(f"DELETE FROM Cadastro WHERE ID = ?", [id])
            conexao.commit()
            print('\nExcluido com Sucesso !')

        else:
            pass

    def sair(self):
        conexao.close()
        print('\nAté a proxima !\n')
        exit()