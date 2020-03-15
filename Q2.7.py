'''7 - Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#DaniloSouza #14/03/2020
'''variável n = número'''

n1 = int(input("Insira seu primeiro número: "))
n2 = int(input("Insira seu segundo número: "))
n3 = int(input("Insira seu terceiro número: "))

if n1 > n2 > n3:
	print("O maior número é %d" % n1)
	print("O menor número é %d" % n3)
elif n1 > n3 > n2:
	print("O maior número é %d" % n1)
	print("O menor número é %d" % n2)
elif n2 > n1 > n3:
	print("O maior número é %d" % n2)
	print("O menor número é %d" % n3)
elif n2 > n3 > n1:
	print("O maior número é %d" % n2)
	print("O menor número é %d" % n1)
elif n3 > n1 > n2:
	print("O maior número é %d" % n3)
	print("O menor número é %d" % n2)
elif n3 > n2 > n1:
	print("O maior número é %d" % n3)
	print("O menor número é %d" % n1)
