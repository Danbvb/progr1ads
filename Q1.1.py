#Exercio 04/03/2020
#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.
#DaniloSouza #11/03/2020 
valor_usuario = float(input("Insira o valor da desejado em reais: "))
valor_combustivel = float(input("Insira o valor da gasolina: "))
valor_final = valor_usuario / valor_combustivel

print (" A quantidade de será de %.2fLt" % valor_final)

