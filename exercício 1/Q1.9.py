'''9 - Escreva um programa que converte valores de polegadas 
em centímetros utilizando a seguinte fórmula: 1 polegada = 2,54cm;'''
'''Danilo Souza - 14/04/2020'''

#cm = centímetro
#in = polegada
#Função chamada para fazer condições de escolha para selecionar qual conversão utilizar.
def options(choose):
# Se a opção 1 for escolhida será pedido o valor da conversão em polegadas para cm.    
    if choose == 1:
#Ler a variável inch que pede o valor informado pelo usuário.
        inch = float(input("Informe o valor em polegadas: "))
#Chamar a função onde será feita a inch_to_cm.
        inch_to_cm(inch)
#Se a condição 2 for escolhida o valor de centímetros será convertido para polegadas.
    elif choose == 2:
#Ler a variável cm que pede o valor informado pelo usuário.
        cm = float(input("Informe o valor em centímetros: "))
#Chamar a função onde será feita a conversão cm_to_inch
        cm_to_inch(cm)

#Chamar condição se o valor informado em choose não for 1 ou 2.
    else:
        print('valor inválido')

#Função onde será efetuada a conversão de polegadas para cm.
def inch_to_cm(inch):
#Valor padrão de 1 polegada para centímetro.
    cm = 2.54
#variável onde será feita o cálculo da conversão 
    conversor = inch * cm
#Exibir o resultado da conversão e o valor apresentado pelo usuário
    print("o valor %.2f in é %.2f cm" % (inch, conversor))

#Função para fazer a conversão de centímetros para polegadas
def cm_to_inch(cm):
#Variável onde é armazenada o valor padrão da conversão
    inch = 2.54
#Variável onde será feito o cálculo de conversão
    conversor = cm / inch
#Exibir o resultado da conversão e o valor apresentado pelo usuário
    print("o valor %.2f cm é %.2f in" % (cm, conversor))

#Função principal do script
def main():
#Imprimir o nome do programa e as 2 opções de conversões
    print("CONVERSOR DE ÁREA")
    print("1 PARA POLEGADAS PARA CM ")
    print("2 PARA CM PARA POLEGADAS")
#Variável onde será armazenada a opção do usuário
    choose = int(input("> "))
#Chamar a função de condições de escolhas
    options(choose)

#chamar função principal do script
main()

