from Controlador import Banco

banco = Banco()

def main():
    print('\n\t Bem vindo ao Menu de cadastro')

    while True:
        print('\n01-Cadastro | 02-Atualizar | 03-Consultar | 04-Excluir | 05-Sair')
        opcao = int(input('\nOpcao: '))
        if opcao == 1:
            nome = input("Nome: ")
            idade = input("Idade: ")
            banco.set_Cadastro(nome, idade)

        elif opcao == 2:
            banco.get_Valores()
            id = input('\nInforme ID que deseja alterar: ')
            novo_nome = input('Nome: ')
            nova_idade = input('Idade: ')
            banco.set_update(novo_nome, nova_idade, id)

        elif opcao == 3:
            banco.get_Valores()

        elif opcao == 4:
            banco.get_Valores()
            acao = input('\nInforma ID que deseja Excluir: ')
            banco.set_excluir(acao)

        elif opcao == 5:
            acao = input('\nDeseja Sair Sim/Nao: ')
            if acao.lower() == 's' or acao.lower() == 'sim':
                banco.sair()
            else:
                pass
        else:
            print('\nOpção Invalida !')

main()


# Sisteminha simples para portifolio.

# Utilização do SLQLITE + Panda.