'''Exercio 04/03/2020
1. Faça um programa que solicite ao usuário o valor do litro de combustível
(ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00).
Calcule quantos litros de combustível o usuário obterá com esses valores.
DaniloSouza 11/03/2020 '''

#Função no qual será feito o cálculo e a exibição do valor.
def value_per_lt(valor_usuario, valor_combustivel):
    #Fórmula para calcular a simulação do usuário no qual o valor do usuário é dividido pelo combustível
    valor_final = valor_usuario / valor_combustivel
    #Exibir o resultado do cálculo e determinando o fim do programa.
    print("Com o valor de R$%.2f teremos %.2f Lt" % (valor_usuario, valor_final))

#Função principal onde contêm as variáveis que serão utilizadas na função value_per_lt
def main():
    #Variável onde armazena o valor em dinheiro que o usuário para ser usado na simulação
    valor_usuario = float(input("Insira o valor da desejado em reais: "))
    #Variável onde será armazenado o valor do litro da galosina informado pelo cliente 
    valor_combustivel = float(input("Insira o valor do litro da gasolina: "))
    #chamar a função value_per_lt onde será feito os cálculos
    value_per_lt(valor_usuario, valor_combustivel)

#chamar a função principal
main()

