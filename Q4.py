#Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.
#DaniloSouza #11/03/2020
F = int(input("Insira a temperatura em fahrenheit: "))
C = ( F - 32 ) * 5 / 9
print ("A temperatura em Celsius será de %.2f" % C)
