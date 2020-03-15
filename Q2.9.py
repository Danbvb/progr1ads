'''9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
'''DaniloSouza 14/03/2020'''
#variavel n = número

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if n3 < n2 < n1:
    print(n3, n2, n1)
elif n3 < n1 < n2:
    print(n3, n1, n2)
elif n2 < n3 < n1:
    print(n2, n3, n1)
elif n2 < n1 < n2:
    print(n2, n3, n1)
elif n1 < n2 < n3:
    print(n1, n2, n3)
elif n1 < n3 < n2:
    print(n1, n3, n2)

