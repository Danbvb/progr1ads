'''2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''
#DaniloSouza #14/03/2020

#Função onde indicará se o número é positivo, neutro ou negativo.
def number(valor):
	#Condição onde número fornecido pelo usuário será maior que 0
	if valor > 0:
		#Exibir que o número é positvo
		print("O número é positivo")
	#Condição onde número fornecido pelo usuário é neutro, ou seja, é igual a 0
	elif valor == 0:
		#Exibir que o número é neutro
		print("O número é neutro")
	#Condição onde número fornecido pelo usuário é negativo.
	else:
		#Exibir que o número negativo
		print("O número é negativo")

#Função principal 
def main():
	#Variável onde armazenará o valor fornecido pelo usuário
	valor = int(input("Insira um número desejado: "))
	#chamar função number
	number(valor)

#chamar função principal
main()

