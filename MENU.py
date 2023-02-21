def menuPrincipal():
    while True:
        print("[1] - Fazer pedido")
        print("[2] - Ver promoções")
        print("[3] - Editar pedido")
        print("[4] - Remover item")
        print("[5] - Finalizar compra")
        opcaoMenu = int(input("Escolha uma opção:"))
        return opcaoMenu
