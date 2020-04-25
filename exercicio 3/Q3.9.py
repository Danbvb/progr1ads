'''9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
'''DaniloSouza 14/03/2020'''
#variavel n = número

#Função onde terá as condições para listar a ordem descrente
def order(n1, n2, n3):
    #Se n3 for menor que n2 menor que n1
    if n3 < n2 < n1:
        #Exibir a sequência n3 < n2 < n1
        print(n3, n2, n1)
    #Se n3 for menor que n1 menor que n2
    elif n3 < n1 < n2:
        #Exibir a sequência n3 < n1 < n2
        print(n3, n1, n2)
    #Se n2 for menor que n3 menor que n1
    elif n2 < n3 < n1:
        #Exibir a sequência n2 < n3 < n1
        print(n2, n3, n1)
    #Se n2 for menor que n1 menor que n3
    elif n2 < n1 < n3:
        #Exibir a sequência n2 < n1 < n3 
        print(n2, n1, n3)
    #Se n1 for menor que n2 menor que n3
    elif n1 < n2 < n3:
        #exibir a sequência n1 < n2 < n3
        print(n1, n2, n3)
    #Se n1 for menor que n3 menor que n2
    elif n1 < n3 < n2:
        #exibir a sequência n1 < n3 < n2
        print(n1, n3, n2)

#Função principal
def main():
    #Variável onde armazena o primeiro número fornecido pelo usuário
    n1 = int(input("Insira o primeiro número: "))
    #Variável onde armazena o segundo número fornecido pelo usuário
    n2 = int(input("Insira o segundo número: "))
    #Variável onde armazena o terceiro número fornecido pelo usuário
    n3 = int(input("Insira o terceiro número: "))
    #Chamar a função order
    order(n1, n2, n3)
    
#chamar função principal
main()
