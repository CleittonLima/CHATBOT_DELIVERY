def tamanhoCoca():
    while True:
        print("-=" * 25)
        print("TAMANHO DA COCA COLA")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("Num:", "Item:", "L/ML", "Preço:"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("1", "Latinha", "350ml", "R$ 4,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("2", "Garrafa", "2l", "R$ 7,99"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("3", "Garafa de Vidro", "1l", "R$ 6,50"))
        tamCoca = int(input("Escolha o Tamanho da Bebida:"))

        if tamCoca == 1:
            sabor = cocaLata350()

        elif tamCoca == 2:
            sabor = coca2l()

        elif tamCoca == 3:
            sabor = coca1l()

        else:
            print("Digite um número válido!!")
            return tamanhoCoca()
        precoCoca = {"Latinha 350": 4.50, "Garrafa 2l": 7.99, "Garrafa vidro 1l": 6.50}
        listadeSabores = ["Original","Zero","Limão","Cereja"]
        lista = [[f'Coca-Cola {listadeSabores[sabor-1]}'],[list(precoCoca.keys())[tamCoca - 1]],[precoCoca.get(list(precoCoca.keys())[tamCoca - 1])]]
        return lista


def cocaLata350():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 350ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Zero"))
        print("{0:<10}{1:<20}".format("3", "Limão"))
        print("{0:<10}{1:<20}".format("4", "Cereja"))
        saborCoca = int(input("Escolha o sabor da Coca Cola:"))
        if saborCoca == 1:
            print("Coca Cola 350ml sabor Original adicionada!")

        elif saborCoca == 2:
            print("Coca Cola 350ml sabor Zero adicionada!")

        elif saborCoca == 3:
            print("Coca Cola 350ml sabor Limão adicionada!")

        elif saborCoca == 4:
            print("Coca Cola 350ml sabor Cereja adicionada!")

        else:
            print("Digite um número válido!!")
            return cocaLata350()

        return saborCoca

def coca2l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA 2l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Zero"))
        print("{0:<10}{1:<20}".format("3", "Limão"))
        print("{0:<10}{1:<20}".format("4", "Cereja"))
        saborCoca = int(input("Escolha o sabor da Coca Cola:"))
        if saborCoca == 1:
            print("Coca Cola 2l sabor Original adicionada!")

        elif saborCoca == 2:
            print("Coca Cola 2l sabor Zero adicionada!")

        elif saborCoca == 3:
            print("Coca Cola 2l sabor Limão adicionada!")

        elif saborCoca == 4:
            print("Coca Cola 2l sabor Cereja adicionada!")

        else:
            print("Digite um número válido!!")
            return coca2l()

        return saborCoca

def coca1l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Zero"))
        print("{0:<10}{1:<20}".format("3", "Limão"))
        print("{0:<10}{1:<20}".format("4", "Cereja"))
        saborCoca = int(input("Escolha o sabor da Coca Cola:"))
        if saborCoca == 1:
            print("Coca Cola 1l sabor Original adicionada!")

        elif saborCoca == 2:
            print("Coca Cola 1l sabor Zero adicionada!")

        elif saborCoca == 3:
            print("Coca Cola 1l sabor Limão adicionada!")

        elif saborCoca == 4:
            print("Coca Cola 1l sabor Cereja adicionada!")

        else:
            print("Digite um número válido!!")
            return coca1l()

        return saborCoca

#===============================================================================================================
def tamanhoFanta():
    while True:
        print("-=" * 25)
        print("TAMANHO DA FANTA")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("Num:", "Item:", "L/ML", "Preço:"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("1", "Latinha", "350ml", "R$ 3,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("2", "Latinha", "220ml", "R$ 1,99"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("3", "Garrafa", "2l", "R$ 6,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("4", "Garafa de Vidro", "1l", "R$ 4,50"))
        tamFanta = int(input("Escolha o Tamanho da Bebida:"))

        if tamFanta == 1:
            sabor = fantaLata350()

        elif tamFanta == 2:
            sabor = fantaLata220()

        elif tamFanta == 3:
            sabor = fanta2l()

        elif tamFanta == 4:
            sabor = fanta1l()

        else:
            print("Digite um número válido!!")
            return tamanhoFanta()

        precoFanta = {"Latinha 350": 3.50, "Latinha 220": 1.99, "Garrafa 2l": 6.50, "Garrafa vidro 1l": 4.50}
        listadeSabores = ["Laranja", "Limão", "Uva", "Framboesa"]
        lista = [[f'Fanta {listadeSabores[sabor - 1]}'], [list(precoFanta.keys())[tamFanta - 1]],
                 [precoFanta.get(list(precoFanta.keys())[tamFanta - 1])]]
        return lista

def fantaLata350():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 350ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Laranja"))
        print("{0:<10}{1:<20}".format("2", "limão"))
        print("{0:<10}{1:<20}".format("3", "Uva"))
        print("{0:<10}{1:<20}".format("4", "Framboesa"))
        saborFanta = int(input("Escolha o sabor da Fanta:"))
        if saborFanta == 1:
            print("Fanta 350ml sabor Laranja adicionada!")

        elif saborFanta == 2:
            print("Fanta 350ml sabor Limão adicionada!")

        elif saborFanta == 3:
            print("Fanta 350ml sabor Uva adicionada!")

        elif saborFanta == 4:
            print("Fanta 350ml sabor Framboesa adicionada!")

        else:
            print("Digite um número válido!!")
            return fantaLata350()
        return saborFanta

def fantaLata220():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 220ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Laranja"))
        print("{0:<10}{1:<20}".format("2", "limão"))
        print("{0:<10}{1:<20}".format("3", "Uva"))
        print("{0:<10}{1:<20}".format("4", "Framboesa"))
        saborFanta = int(input("Escolha o sabor da Fanta:"))
        if saborFanta == 1:
            print("Fanta 350ml sabor Laranja adicionada!")

        elif saborFanta == 2:
            print("Fanta 350ml sabor Limão adicionada!")

        elif saborFanta == 3:
            print("Fanta 350ml sabor Uva adicionada!")

        elif saborFanta == 4:
            print("Fanta 350ml sabor Framboesa adicionada!")

        else:
            print("Digite um número válido!!")
            return fantaLata220()
        return saborFanta

def fanta2l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA 2l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Laranja"))
        print("{0:<10}{1:<20}".format("2", "limão"))
        print("{0:<10}{1:<20}".format("3", "Uva"))
        saborFanta = int(input("Escolha o sabor da Fanta:"))
        if saborFanta == 1:
            print("Fanta 350ml sabor Laranja adicionada!")

        elif saborFanta == 2:
            print("Fanta 350ml sabor Limão adicionada!")

        elif saborFanta == 3:
            print("Fanta 350ml sabor Uva adicionada!")

        else:
            print("Digite um número válido!!")
            return fanta2l()
        return saborFanta

def fanta1l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Laranja"))
        print("{0:<10}{1:<20}".format("2", "limão"))
        print("{0:<10}{1:<20}".format("3", "Uva"))
        saborFanta = int(input("Escolha o sabor da Fanta:"))
        if saborFanta == 1:
            print("Fanta 350ml sabor Laranja adicionada!")

        elif saborFanta == 2:
            print("Fanta 350ml sabor Limão adicionada!")

        elif saborFanta == 3:
            print("Fanta 350ml sabor Uva adicionada!")

        else:
            print("Digite um número válido!!")
            return fanta1l()
        return saborFanta

#=================================================================================================================
def tamanhoPepsi():
    while True:
        print("-=" * 25)
        print("TAMANHO DA PEPSI")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("Num:", "Item:", "L/ML", "Preço:"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("1", "Latinha", "350ml", "R$ 3,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("2", "Latinha", "220ml", "R$ 1,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("3", "Garrafa", "2l", "R$ 5,99"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("4", "Garafa de Vidro", "1l", "R$ 4,50"))
        tamPepsi = int(input("Escolha o Tamanho da Bebida:"))


        if tamPepsi == 1:
            sabor = pepsiLata350()

        elif tamPepsi == 2:
            sabor = pepsiLata220()

        elif tamPepsi == 3:
            sabor = pepsi2l()

        elif tamPepsi == 4:
            sabor = pepsi1l()

        else:
            print("Digite um número válido!!")
            return tamanhoPepsi()


        precoPepsi = {"Latinha 350": 3.50, "Latinha 220": 1.50, "Garrafa 2l": 5.99, "Garrafa vidro 1l": 4.50}
        listadeSabores = ["Original", "Black", "Descafeinado", "Cereja baunilha"]
        lista = [[f'Pepsi {listadeSabores[sabor - 1]}'], [list(precoPepsi.keys())[tamPepsi - 1]],
                 [precoPepsi.get(list(precoPepsi.keys())[tamPepsi - 1])]]
        return lista

def pepsiLata350():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 350ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Black"))
        print("{0:<10}{1:<20}".format("3", "Descafeinado"))
        print("{0:<10}{1:<20}".format("4", "Cereja Baunilha"))
        saborPepsi = int(input("Escolha o sabor da Pepsi:"))
        if saborPepsi == 1:
            print("Pepsi 350ml sabor Original adicionada!")

        elif saborPepsi == 2:
            print("Pepsi 350ml sabor Black adicionada!")

        elif saborPepsi == 3:
            print("Pepsi 350ml sabor Descafeinado adicionada!")

        elif saborPepsi == 4:
            print("Pepsi 350ml sabor Cereja Baunilha adicionada!")

        else:
            print("Digite um número válido!!")
            return pepsiLata350()
        return saborPepsi

def pepsiLata220():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 220ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Black"))
        print("{0:<10}{1:<20}".format("3", "Descafeinado"))
        print("{0:<10}{1:<20}".format("4", "Cereja Baunilha"))
        saborPepsi = int(input("Escolha o sabor da Pepsi:"))
        if saborPepsi == 1:
            print("Pepsi 220ml sabor Original adicionada!")

        elif saborPepsi == 2:
            print("Pepsi 220ml sabor Black adicionada!")

        elif saborPepsi == 3:
            print("Pepsi 220ml sabor Descafeinado adicionada!")

        elif saborPepsi == 4:
            print("Pepsi 220ml sabor Cereja Baunilha adicionada!")

        else:
            print("Digite um número válido!!")
            return pepsiLata220()
        return saborPepsi

def pepsi2l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA 2l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Black"))
        saborPepsi = int(input("Escolha o sabor da Pepsi:"))
        if saborPepsi == 1:
            print("Pepsi 2l sabor Original adicionada!")

        elif saborPepsi == 2:
            print("Pepsi 2l sabor Black adicionada!")

        else:
            print("Digite um número válido!!")
            return pepsi2l()
        return saborPepsi

def pepsi1l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Original"))
        print("{0:<10}{1:<20}".format("2", "Black"))
        saborPepsi = int(input("Escolha o sabor da Pepsi:"))
        if saborPepsi == 1:
            print("Pepsi 1l sabor Original adicionada!")

        elif saborPepsi == 2:
            print("Pepsi 1l sabor Black adicionada!")

        else:
            print("Digite um número válido!!")
            return pepsi1l()
        return saborPepsi
#==============================================================================================================
def tamanhoGuarana():
    while True:
        print("-=" * 25)
        print("TAMANHO DO GUARANÁ")
        print("-=" * 25)
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("Num:", "Item:", "L/ML", "Preço:"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("1", "Latinha", "350ml", "R$ 4,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("2", "Latinha", "220ml", "R$ 1,99"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("3", "Garrafa", "2l", "R$ 7,50"))
        print("{0:<10}{1:<20}{2:>5}{3:>10}".format("4", "Garafa de Vidro", "1l", "R$ 5,50"))
        tamGuara = int(input("Escolha o Tamanho da Bebida:"))

        if tamGuara == 1:
            sabor = guaranaLata350()

        elif tamGuara == 2:
            sabor = guaranaLata220()

        elif tamGuara == 3:
            sabor = guarana2l()

        elif tamGuara == 4:
            sabor = guarana1l()

        else:
            print("Digite um número válido!!")
            return tamanhoGuarana()

        precoGuarana = {"Latinha 350": 4.50, "Latinha 220": 1.99, "Garrafa 2l": 7.50, "Garrafa vidro 1l": 5.50}
        listadeSabores = ["Guaraná", "Cajá", "Uva verde", "Acerola"]
        lista = [[f'Guaraná {listadeSabores[sabor - 1]}'], [list(precoGuarana.keys())[tamGuara - 1]],
                 [precoGuarana.get(list(precoGuarana.keys())[tamGuara - 1])]]
        return lista

def guaranaLata350():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 350ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Guaraná"))
        print("{0:<10}{1:<20}".format("2", "Cajá"))
        print("{0:<10}{1:<20}".format("3", "Uva Verde"))
        print("{0:<10}{1:<20}".format("4", "Acerola"))
        saborGuarana = int(input("Escolha o sabor do Guaraná:"))
        if saborGuarana == 1:
            print("Guaraná 350ml sabor Guaraná adicionada!")

        elif saborGuarana == 2:
            print("Guaraná 350ml sabor Cajá adicionada!")

        elif saborGuarana == 3:
            print("Guaraná 350ml sabor Uva Verde adicionada!")

        elif saborGuarana == 4:
            print("Guaraná 350ml sabor Acerola adicionada!")

        else:
            print("Digite um número válido!!")
            return guaranaLata350()
        return saborGuarana

def guaranaLata220():
    while True:
        print("-=" * 25)
        print("SABORES LATINHA 220ml")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Guaraná"))
        print("{0:<10}{1:<20}".format("2", "Cajá"))
        print("{0:<10}{1:<20}".format("3", "Uva Verde"))
        print("{0:<10}{1:<20}".format("4", "Acerola"))
        saborGuarana = int(input("Escolha o sabor do Guaraná:"))
        if saborGuarana == 1:
            print("Guaraná 220ml sabor Guaraná adicionada!")

        elif saborGuarana == 2:
            print("Guaraná 220ml sabor Cajá adicionada!")

        elif saborGuarana == 3:
            print("Guaraná 220ml sabor Uva Verde adicionada!")

        elif saborGuarana == 4:
            print("Guaraná 220ml sabor Acerola adicionada!")

        else:
            print("Digite um número válido!!")
            return guaranaLata220()
        return saborGuarana

def guarana2l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA 2l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Guaraná"))
        print("{0:<10}{1:<20}".format("2", "Cajá"))
        saborGuarana = int(input("Escolha o sabor do Guaraná:"))
        if saborGuarana == 1:
            print("Guaraná 2l sabor Guaraná adicionada!")

        elif saborGuarana == 2:
            print("Guaraná 2l sabor Cajá adicionada!")

        else:
            print("Digite um número válido!!")
            return guarana2l()
        return saborGuarana

def guarana1l():
    while True:
        print("-=" * 25)
        print("SABORES GARRAFA DE VIDRO 1l")
        print("-=" * 25)
        print("{0:<10}{1:<20}".format("Num:", "Sabor:"))
        print("{0:<10}{1:<20}".format("1", "Guaraná"))
        print("{0:<10}{1:<20}".format("2", "Cajá"))
        saborGuarana = int(input("Escolha o sabor do Guaraná:"))
        if saborGuarana == 1:
            print("Guaraná 1l sabor Guaraná adicionada!")

        elif saborGuarana == 2:
            print("Guaraná 1l sabor Cajá adicionada!")

        else:
            print("Digite um número válido!!")
            return guarana1l()
        return saborGuarana