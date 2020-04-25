''' 6 - Faça um Programa que leia três números e mostre o maior deles.'''
#DaniloSouza #14/03/2020
'''variável n = número'''

#Função number onde terá as condições para saber qual é o maior número fornecido pelo usuário
def number(n1, n2, n3):
	#Se n1 for maior que n2 e n3 
	if n1 > n2 and n3:
		#Exibir que o maior número é o n1
		print("O maior número é %d" % n1)
	#Se n2 for maior que n1 e n3
	elif n2 > n1 and n3:
		#Exibir que o maior número é o n2
		print("O maior número é %d" % n2)
	#Se n3 for maior que n1 e n2
	elif n3 > n1 and n2:
		#Exibir que o maior número é o n3
		print("O maior número é %d" % n3)

#Função principal
def main():
	#Variável será armazenada o primeiro número fornecido pelo usuário
	n1 = int(input("Insira seu primeiro número: "))
	#Variável será armazenada o segundo número fornecido pelo usuário
	n2 = int(input("Insira seu segundo número: "))
	#Variável será armazenada o terceiro número fornecido pelo usuário
	n3 = int(input("Insira seu terceiro número: "))
	#chamar função number
	number(n1, n2, n3)

#chamar função principal 
main()
	
