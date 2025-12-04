from Controlador import Banco

banco = Banco()

def main():
    print('\n\t Bem vindo ao Menu de cadastro')

    while True:
        try:
            print('\n1-Cadastro | 2-Atualizar | 3-Consultar | 4-Excluir | 5-Sair')
            opcao = int(input('\nOpcao: '))
            if opcao == 1:
                nome = input("Nome: ")
                idade = input("Idade: ")
                banco.set_Cadastro(nome, idade)

            elif opcao == 2:
                banco.get_Valores()
                id = input('\nID que deseja alterar: ')
                novo_nome = input('Nome: ')
                nova_idade = input('Idade: ')
                banco.set_update(novo_nome, nova_idade, id)

            elif opcao == 3:
                banco.get_Valores()

            elif opcao == 4:
                banco.get_Valores()
                acao = input('\nID que deseja Excluir: ')
                banco.set_excluir(acao)

            elif opcao == 5:
                acao = input('\nDeseja Sair: Sim / Nao: ').lower()
                if acao== 's' or acao == 'sim':
                    banco.sair()
                else:
                    pass
            else:
                print('\nOpção Invalida !')

        except KeyboardInterrupt:
            banco.sair()

main()