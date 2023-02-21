from MENU import menuPrincipal
import FUNCOES

FUNCOES.cadastrarCliente()
def main():

    while True:
        opcaoMenu = menuPrincipal()
        if opcaoMenu == 1:
            FUNCOES.fazerPedido()

        elif opcaoMenu == 2:
            FUNCOES.promocao()

        elif opcaoMenu == 3:
            FUNCOES.editarPedido()

        elif opcaoMenu == 4:
            FUNCOES.removerPedido()

        elif opcaoMenu == 5:
            FUNCOES.finalizerCompra()
            print("Aplicação finalizada!")
            break

        else:
            print("Opção inválida!!")


main()
