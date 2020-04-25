'''6 - Escreva um programa que leia uma temperatura
 em graus Fahrenheit, transforme-a em graus Celsius 
 e exiba o resultado.'''
#Função para fazer conversão da temperatura
def temperatura(entrada_F):
    #Formula de conversão de Fahrenheit para Celsius com a fórmula: (F - 32)*/9
    celsius = (entrada_F - 32) * 5 / 9
    #Exibir na tela o resultado da conversão de Fahrenheit para Celsius
    print("A temperatura será de %.3fºC" % celsius)
#Função principal 
def main():
    #Armazenar os dados que vão entrar na variável entrada_F
    entrada_F = float(input("Informe o valor da temporada em ºF: "))
    #Chamar a função temperatura
    temperatura(entrada_F)
#Chamar função principal
main()

