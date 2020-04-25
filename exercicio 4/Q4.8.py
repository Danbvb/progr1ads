'''8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''
#DaniloSouza #18/03/2020

#Função onde terá as condições 
def date():
        #Se mes for igual a 1, 3, 5, 7, 8, 10, 12
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                #Se dia for menor igual a 31
                if dia<=31:
                        #Exibir data válida
                        print("data válida")
                #Senão
                else:
                        #Exibir data inválida
                        print("data inválida")
        #Se mes for igual 2
        elif mes == 2:
                #Se dia for menor igual a 28
                if dia <=28:
                        #Exibir data válida
                        print("data válida")
                #Senão
                else:
                        #Exibir data inválida
                        print("data inválida")
        #Se mes for igual a 4, 6, 9 e 11
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                #Se dia for menor igual a 30
                if dia <=30:
                        #Exibir data válida
                        print ("data válida")
                #Senão 
                else:
                        #Exibir data inválida
                        print ("data inválida")

#função principal
def main():
        #Variável dia que será fornecida pelo usuário
        dia = int(input("Insira o dia que você deseja: "))
        #Variável mês que será fornecida pelo usuário
        mes = int(input("Insira o mês que você deseja: "))
        #Variável ano que será fornecida 
        ano = int(input("Insira o ano que você deseja: "))
        #chamar função date
        date(dia, mes, ano)
#chamar função principal
main()