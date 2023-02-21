from MENU_F import menuPrincipal
import FUNCOES_F2

FUNCOES_F2.cadastrarCliente()
def main():

    while True:
        opcaoMenu = menuPrincipal()
        if opcaoMenu == 1:
            FUNCOES_F2.fazerPedido()

        elif opcaoMenu == 2:
            FUNCOES_F2.promocao()

        elif opcaoMenu == 3:
            FUNCOES_F2.editarPedido()

        elif opcaoMenu == 4:
            FUNCOES_F2.removerPedido()

        elif opcaoMenu == 5:
            FUNCOES_F2.finalizerCompra()
            print("Aplicação finalizada!")
            break

        else:
            print("Opção inválida!!")


main()
