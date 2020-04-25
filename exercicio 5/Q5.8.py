'''8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
#Danilo Souza 24/04/2020

numero = 0

for n in range(5):
    num = int(input("informe um número: "))
    numero += num
media = numero // 5
print('soma dos números é %d' % numero)
print('a media dos números é %d' % media)