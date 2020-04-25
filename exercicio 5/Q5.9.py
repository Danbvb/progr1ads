'''(1.50) 9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50 '''
#Danilo Souza #24/04/2020.
 
alance = int(input('informe o alcance final: '))
for x in range(1, alance):
    if x % 2 != 0:
        print(x)

