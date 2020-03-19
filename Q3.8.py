'''8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''
#DaniloSouza #18/03/2020

dia = int(input("Insira o dia que você deseja: "))
mes = int(input("Insira o mês que você deseja: "))
ano = int(input("Insira o ano que você deseja: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia<=31:
                print("data válida")
        else:
                print("data inválida")
elif mes ==2:
        if dia <=28:
                print("data válida")
        else:
                print("data inválida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <=30:
                print ("data válida")
        else:
                print ("data inválida")
