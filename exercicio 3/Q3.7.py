'''7 - Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#DaniloSouza #14/03/2020
#variável n = número

#Função onde tem as condições para saber qual o número é o maior
def number(n1, n2, n3):
	#Se o n1 for maior que n2 que é maior que n3
	if n1 > n2 > n3:
		#Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n1, n3))
	#Se o n1 for maior que n3 que é maior que n2
	elif n1 > n3 > n2:
		#Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n1, n2))
	#Se o n2 for maior que n1 que é maior que n3
	elif n2 > n1 > n3: 
		 # Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n2, n3))
	#Se o n2 for maior que n3 que é maior que n1
	elif n2 > n3 > n1:
		#Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n2, n1))
	#Se o n3 for maior que n1 que é maior que n2
	elif n3 > n1 > n2:
		#Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n3, n2))
	#Se o n3 for maior que n2 que é maior que n1
	elif n3 > n2 > n1:
		#Exibir o maior e o menor número
		print("O maior número é %d e o menor %d " % (n3, n1))

#função principal 
def main():
	#Variável onde o usuário vai fornecer o primeiro número
	n1 = int(input("Insira seu primeiro número: "))
	#Variável onde o usuário vai fornecer o segundo número
	n2 = int(input("Insira seu segundo número: "))
	#Variável onde o usuário vai fornecer o terceiro número
	n3 = int(input("Insira seu terceiro número: "))
	number(n1, n2, n3)
	
#chamar função principal 
main()
