''' 8 - Escreva um programa que leia um valor inteiro e calcule o seu cubo.'''
'''Danilo Souza - 08/04/2020'''

#Função onde será feito o cálculo do quadrado
def quadrado(valor_entrance, valor_exponciancao):
    #Formúla para encontrar o quadrado da variável valor_entrance.
    quadrado = valor_entrance ** 2
    #Exibir o resultado do quadrado.
    print("O quadrado do valor %d é %d" % (valor_entrance, quadrado))

#Função onde será feito o cálculo do cubo
def cubo(valor_entrance, valor_exponciancao):
    #Formúla para encontrar o cubo da variável valor_entrance.
    cubo = valor_entrance ** 3
    #Exibir o resultado do cubo.
    print("O cubo do valor %d é %d" % (valor_entrance, cubo))

#Função principal
def main():
    #Variável onde armazenará o valor desejado do usuário para exponcianção
    valor_entrance = int(input("Informe o valor para calcular: "))
    #Variável onde armazenará o valor da exponenciação em que o usuário vai utilizar
    valor_exponciancao = int(input("Informe o valor da exponianção: "))
    #Condição para caso seja um quadrado
    if valor_exponciancao == 2:
        #Chamar a função quadrado
        quadrado(valor_entrance, valor_exponciancao)
    #Condição para caso seja um cubo
    elif valor_exponciancao == 3:
        #Chamar função cubo
        cubo(valor_entrance, valor_exponciancao)


#Chamar função principal
main()

