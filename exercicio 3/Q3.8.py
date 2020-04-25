'''8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
 sabendo que a decisão é sempre pelo mais barato.'''
'''Danilo Souza 14/03/2020'''

#Função onde terá as condições para identificar o prodeto mais barato
def value(p1, p2, p3, moeda):
        #Se o p1 for menor que p2 e p3
        if p1 < p2 and p3:
                #Exibir que p1 é o produto mais barato
                print("O produto mais barato é o primeiro produto com o valor de %.2f em %s" % (p1, moeda))
        #Se o p2 for menor que p1 e p3
        elif p2 < p1 and p3:
                #Exibir que p2 é o produto mais barato
                print("O produto mais barato é o segundo produto com o valor de %.2f em %s" % (p2, moeda))
        #Se o p3 for que menor p1 e p2
        elif p3 < p2 and p1:
                #Exibir que p3 é o produto mais barato
                print("O produto mais barato é o terceiro produto com o valor de %.2f em %s" % (p3, moeda))
        #Se o p1 for igual ao p2 e menor que p3 
        elif p1 == p2 < p3:
                #Exibir que p1 e p2 são os produtos mais baratos
                print("Os produtos mais baratos são os produtos nos valores de %.2f e o %.2f em %s" % (p1, p2, moeda))
        #Se p1 for igual a p3 e menor que p2
        elif p1 == p3 < p2:
                #Exibir que p1 e p3 são os produtos mais baratos
                print("Os produtos mais baratos são os produtos nos valores de %.2f e o %.2f em %s" % (p1, p3, moeda))
        #Se p2 for igual a p3 e mnor que p2
        elif p2 == p3 < p1:
                #Exibir que p2 e p3 são os produtos mais baratos
                print("Os produtos mais baratos são os produtos nos valores de  %.2f e o %.2f em %s" % (p2, p3, moeda))
        #Senão
        else:
                #Exibir que os produtos tem o mesmo valor
                print("Todos os valores se equivalem em %s " % moeda)

#Função principal
def main():
        #Variável onde será armazenado o valor do primeiro produto fornecido pelo usuário
        p1 = float(input("Informe o valor do primeiro produto: "))
        #Variável onde será armazenado o valor do segundo produto fornecido pelo usuário
        p2 = float(input("Informe o valor do segundo produto: "))
        #Variável onde será armazenado o valor do terceiro produto fornecido pelo usuário
        p3 = float(input("Informe o valor do terceiro produto: "))
        #Variável onde será armazenado a moeda utilizada para compra do produto fornecido pelo usuário
        moeda = str(input("Informe a moeda que você irá utilizar para comprar o produto: "))
        #chamar função number
        number(p1, p2, p3, moeda)
        
#Chamar função principal 
main()


