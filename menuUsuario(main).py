from controladorGerenciamento import *
from controladorOrcamento import *
from bancoDados import *

def main():
    print("===== Bem vindo ao seu gerenciador de ármazem =====")
    meuBanco = BancoDeDados()
    while True:
        try:
            opcao = int(input("-> Menu principal\n[1] - Gerenciar o aramzém\n[2] - Gerenciar orçamentos\n[3] - Sair\n: "))
            if opcao == 1:
                meuArmazem = ControladorGerenciamento(meuBanco)
                meuArmazem.menuGerenciamento()
            elif opcao == 2:
                meuOrcamento = ControladorOrcamento(meuBanco)
                meuOrcamento.menuOrcamento()
            elif opcao == 3:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada Invalida\n.")
main()
