import MENU
import BEBIDAS

lstPedido = [[], [], []]

nome = None
telefone = None
rua = None
numero = None
bairro = None

def cadastrarCliente():
    global numero,telefone,rua,bairro,nome
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    rua = input("Digite sua rua: ")
    numero = input("Digite o número da sua casa: ")
    bairro = input("Digite seu bairro: ")
    return

def fazerPedido():
    while True:
        print("-=" * 25)
        print("Escolha a opção")
        print("-=" * 25)
        print("[1] - Hamburgueres\n[2] - Pizzas\n[3] - Bebidas\n[4] - Voltar ao Menu")
        opcaoPedido = int(input("O que você deseja:"))

        if opcaoPedido == 1:
            hamburguer()

        elif opcaoPedido == 2:
            pizza()

        elif opcaoPedido == 3:
            bebidas()

        elif opcaoPedido == 4:

            return MENU.menuPrincipal()

        else:
            print("Opção Invalida!")
            return fazerPedido()
        break


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def hamburguer():
    while True:

        burguer = ['', 'X-Burguer', 'X-Frango', 'X-Bacon', 'X-Salada']
        print("-=" * 25)
        print("HAMBURGUERES")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}".format("Num:", "Item:", "Preço:"))
        print("{0:<10}{1:<20}{2:>5}".format("1", "X-Burguer", "R$ 10,00"))
        print("{0:<10}{1:<20}{2:>5}".format("2", "X-Frango", "R$ 12,00"))
        print("{0:<10}{1:<20}{2:>5}".format("3", "X-Bacon", "R$ 15,00"))
        print("{0:<10}{1:<20}{2:>5}".format("4", "X-Salada", "R$ 10,00"))

        saborBurguer = int(input("Digite o número do hamburguer que você deseja:"))
        if saborBurguer == 1:
            quantBurgue = int(input("Digite a quantidade de X-Burguer que deseja:"))


        elif saborBurguer == 2:
            quantBurgue = int(input("Digite a quantidade de X-Frango que deseja:"))


        elif saborBurguer == 3:
            quantBurgue = int(input("Digite a quantidade de X-Bacon que deseja:"))


        elif saborBurguer == 4:
            quantBurgue = int(input("Digite a quantidade de X-Salada que deseja:"))


        else:
            print("Digite um número válido!!")
            return hamburguer()

        listadePrecosHamburguers = (10.00, 12.00, 15.00, 10.00)
        lstPedido[0].append(burguer[saborBurguer])
        lstPedido[1].append(quantBurgue)
        lstPedido[2].append(listadePrecosHamburguers[saborBurguer - 1])
        print(quantBurgue, f"{burguer[saborBurguer]} adicionado(s)")

        return


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def pizza():
    while True:
        print("-=" * 25)
        print("SABORES DE PIZZAS")
        print("-=" * 25)
        print("{0:<6}{1:<12}".format("Num:", "Item:"))
        print("{0:<6}{1:<12}".format("1", "Calabresa"))
        print("{0:<6}{1:<12}".format("2", "Moda da casa"))
        print("{0:<6}{1:<12}".format("3", "Mussarela"))
        print("{0:<6}{1:<12}".format("4", "Pepperoni"))
        saborPizza = int(input("Digite o número da Pizza que você deseja:"))
        if saborPizza == 1:

            print("Sabor Calabresa\n")

        elif saborPizza == 2:

            print("Sabor Moda da casa\n")

        elif saborPizza == 3:

            print("Sabor Mussarela\n")

        elif saborPizza == 4:

            print("Sabor Peperone\n")

        else:
            print("Digite um número válido!!")
            return pizza()
        tamanhoPizza(saborPizza)
        break


def tamanhoPizza(saborPizza):
    while True:
        print("-=" * 25)
        print("TAMANHO DA PIZZA")
        print("-=" * 25)
        print("{0:<6}{1:<12}{2:>5}".format("Num:", "Tamanho:", "Preço:"))
        print("{0:<6}{1:<12}{2:>5}".format("1", "Pequena", "R$ 20,00"))
        print("{0:<6}{1:<12}{2:>5}".format("2", "Média", "R$ 30,00"))
        print("{0:<6}{1:<12}{2:>5}".format("3", "Grande", "R$ 45,00"))
        print("{0:<6}{1:<12}{2:>5}".format("4", "Família", "R$ 60,00"))
        tamPizza = int(input("Digite o número do Tamanho da Pizza que você deseja:"))

        if tamPizza == 1:
            print("Pizza tamanho Pequena")

        elif tamPizza == 2:
            print("Pizza tamanho Média")

        elif tamPizza == 3:
            print("Pizza tamanho Grande")

        elif tamPizza == 4:
            print("Pizza tamanho Família")

        else:
            print("Digite um número válido!!")
            return tamanhoPizza(saborPizza)

        listadePizzas = ["pequena","media","grande","familia"]
        precoPizza = [20.00,  30.00, 45.00,  60.00]
        listSabores = ("Calabresa", "Moda da casa", "Mussarela", "Pepperoni")
        lstPedido[0].append(f' {listSabores[saborPizza - 1]}{listadePizzas[tamPizza - 1]}')
        lstPedido[1].append(1) #Quantidade
        lstPedido[2].append(precoPizza[tamPizza - 1])
        print(1, f" pizza {listadePizzas[tamPizza-1]} sabor {listSabores[saborPizza - 1]} adicionado(s)")

        break


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def bebidas():
    while True:
        print("-=" * 25)
        print("BEBIDAS")
        print("-=" * 25)
        print("{0:<6}{1:<12}".format("Num:", "Item:"))
        print("{0:<6}{1:<12}".format("1", "Coca Cola"))
        print("{0:<6}{1:<12}".format("2", "Pepsi"))
        print("{0:<6}{1:<12}".format("3", "Fanta"))
        print("{0:<6}{1:<12}".format("4", "Guaraná"))
        refri = int(input("Digite o refrigerante que você deseja:"))
        if refri == 1:
            lista = BEBIDAS.tamanhoCoca()


        elif refri == 2:
            lista = BEBIDAS.tamanhoPepsi()


        elif refri == 3:
            lista = BEBIDAS.tamanhoFanta()


        elif refri == 4:
            lista = BEBIDAS.tamanhoGuarana()


        else:
            print("Digite um número válido!!")
            return bebidas()

        lstPedido[0].append(f'{lista[1][0]} {lista[0][0]}')
        lstPedido[1].append(1)
        print(lista[2])
        print(lista[2])
        print(lista[2])
        lstPedido[2].append(float(lista[2][0]))
        print(1, f'{lista[1][0]} {lista[0][0]} adicionado(s)')
        return

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def promocao():
    while True:

        print("-=" * 25)
        print("PROMOÇÕES")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("Num:", "Item:", "De:", "Por:"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("1", "Alone", "R$ 45,00", "R$ 30,00"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("2", "Jogatina Solo", "R$50,00", "R$ 40,00"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("3", "A Dupla", "R$ 45,00", "R$ 30,00"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("4", "Jogatina Duo", "R$50,00", "R$ 40,00"))
        opcoesCombo = int(input("Digite o numero do Combo que deseja:"))

        if opcoesCombo == 1:
            print("")
            print("O combo Alone acompanha:\n")
            print("1 - X-Burguer;\n1 - Refrigerante de 1l.")
            escolhaAlone = int(input("Deseja comprar esse combo?\n[1] - Sim\n[2] - Não\nEscolha uma opção:"))
            if escolhaAlone == 1:
                print("Escolha o refri")
                refriCombo()
            else:
                promocao()
        elif opcoesCombo == 2:
            print("")
            print("O combo Jogatina Solo acompanha:\n")
            print("1 - X-Bacon;\n1 - Refrigerante de 1l.\n")
            escolhaAlone = int(input("Deseja comprar esse combo?\n[1] - Sim\n[2] - Não\nEscolha uma opção:"))
            if escolhaAlone == 1:
                print("Escolha o refri")
                refriCombo()
            else:
                promocao()
        elif opcoesCombo == 3:
            print("")
            print("O combo A Dupla acompanha:\n")
            print("2 - X-Burguer;\n1 - Refrigerante de 1l.")
            escolhaAlone = int(input("Deseja comprar esse combo?\n[1] - Sim\n[2] - Não\nEscolha uma opção:"))
            if escolhaAlone == 1:
                print("Escolha o refri")
                refriCombo()
            else:
                promocao()
        elif opcoesCombo == 4:

            print("")
            print("O combo Jogatina Duo acompanha:\n")
            print("2 - X-Bacon;\n1 - Refrigerante de 1l.\n")
            escolhaAlone = int(input("Deseja comprar esse combo?\n[1] - Sim\n[2] - Não\nEscolha uma opção:"))
            if escolhaAlone == 1:
                print("Escolha o refri")
                refriCombo()

            else:
                promocao()
        else:
            print("Digite uma opção válida!!")
            return promocao()

        precoPromo = {"Alone": 30.00, "Jogatina Solo": 40.00, "A Dupla": 30.00, "Jogatina Duo": 40.00}

        lstPedido[0].append(f'{list(precoPromo.keys())[opcoesCombo - 1]}')
        lstPedido[1].append(1)
        lstPedido[2].append(precoPromo.get(list(precoPromo.keys())[opcoesCombo - 1]))
        print(1, f" Combo {list(precoPromo.keys())[opcoesCombo - 1]}  adicionado(s)")
        return


def refriCombo():
    print("-=" * 25)
    print("BEBIDAS")
    print("-=" * 25)
    print("{0:<6}{1:<12}".format("Num:", "Item:"))
    print("{0:<6}{1:<12}".format("1", "Coca Cola"))
    print("{0:<6}{1:<12}".format("2", "Pepsi"))
    print("{0:<6}{1:<12}".format("3", "Fanta"))
    print("{0:<6}{1:<12}".format("4", "Guaraná"))
    refrigeranteCombo = int(input("Digite o refrigerante que deseja: "))
    if refrigeranteCombo == 1:
        refriCocaCombo()


    elif refrigeranteCombo == 2:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Black"))
        saborPepsi = int(input("Escolha o sabor da Pepsi:"))
        if saborPepsi == 1:
            print("Pepsi Original adicionada ao pedido")

        elif saborPepsi == 2:
            print("Pepsi Black adicionada ao pedido")

        else:
            print("Digite uma opção válida!!")
            return refriCombo()

    elif refrigeranteCombo == 3:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Laranja"))
        print("{0:<10}{1:<20}".format("3", "Uva"))
        print("{0:<10}{1:<20}".format("4", "Framboesa"))
        saborFanta = int(input("Escolha o sabor da Fanta:"))
        if saborFanta == 1:
            print("Coca Cola Original adicionada ao pedido")

        elif saborFanta == 2:
            print("Coca Cola Zero adicionada ao pedido")

        else:
            print("Digite uma opção válida!!")
            return refriCombo()


def refriCocaCombo():
    print("-=" * 25)
    print("SABORES GARRAFA DE VIDRO 1l")
    print("-=" * 25)
    print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
    print("{0:<10}{1:<20}".format("1", "Original"))
    print("{0:<10}{1:<20}".format("2", "Zero"))
    saborCoca = int(input("Escolha o sabor da Coca Cola:"))
    if saborCoca == 1:
        print("Coca Cola Original adicionada ao pedido")

    elif saborCoca == 2:
        print("Coca Cola Zero adicionada ao pedido")

    else:
        print("Digite uma opção válida!!")
        return refriCocaCombo()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def editarPedido():
    for i in range(len(lstPedido[0])):
        print(f"[{i}] - Produto: {lstPedido[0][i]}, Quantidade: {lstPedido[1][i]}")
    opcao = int(input("Selecione a opção que quer editar: "))
    opcao2 = int(input("[1] - Produto\n[2] - Quantidade\nDeseja editar: "))
    if opcao2 == 1:
        lstPedido[0].pop(opcao)
        lstPedido[1].pop(opcao)
        lstPedido[2].pop(opcao)
        return fazerPedido()
    elif opcao2 == 2:
        quant = int(input("Escolha nova quantidade: "))
        lstPedido[1][opcao] = quant
        print("Quantidade atualizada")

def removerPedido():
    for i in range(len(lstPedido[0])):
        print(f"[{i}] - Produto: {lstPedido[0][i]}, Quantidade: {lstPedido[1][i]}")
    opcao = int(input("Selecione a opção que quer remover: "))
    confirmacao = int(input("[1] - Sim\n[2] - Não\nTem certeza que quer remover?: "))
    if confirmacao == 1:
        lstPedido[0].pop(opcao)
        lstPedido[1].pop(opcao)
        lstPedido[2].pop(opcao)
        print("Pedido removido!: ")
    elif confirmacao == 2:
        return
    else:
        print("Opção inválida")
        return removerPedido()


def gerarTXT(nome, telefone, rua, numero, bairro):
    arquivo = open('comprovante.txt', 'w')
    arquivo.write(f'nome: {nome}\ntelefone: {telefone}\nrua: {rua}\nnúmero: {numero}\nbairro: {bairro}\n')
    listaparasomar=[]
    for i in range(len(lstPedido[0])):
        valor = (float(lstPedido[1][i]) * (lstPedido[2][i]))
        arquivo.write(f"Produto: {lstPedido[0][i]}, Quantidade: {lstPedido[1][i]}, Valor: {valor}\n")
        listaparasomar.append((lstPedido[1][i]) * (lstPedido[2][i]))
    arquivo.write(f"VALOR TOTAL: {sum(listaparasomar)}\n")


def finalizerCompra():
    listaparasomar = []
    print(f'nome{nome}\n{telefone}\n{rua}\n{numero}\n{bairro}')
    for i in range(len(lstPedido[0])):
        valor = (float(lstPedido[1][i]) * (lstPedido[2][i]))
        print(f"Produto: {lstPedido[0][i]}, Quantidade: {lstPedido[1][i]}, Valor: {valor}")
        listaparasomar.append((lstPedido[1][i]) * (lstPedido[2][i]))
    print(f"VALOR TOTAL:    {sum(listaparasomar)} ")
    gerarTXT (nome, telefone, rua, numero, bairro)