'''1 - Faça um Programa que peça dois números e imprima o maior deles.'''
#DaniloSouza #14/03/2020

#Função onde será identificado o maior número com base nas condições
def maior(valor_1, valor_2): 
	#Condição onde o primeiro valor é maior que o segundo
	if valor_1 > valor_2:
		#Exibir o primeiro valor como sendo o maior
		print("O maior número é %d" % valor_1)
	#Condição onde os valores serão iguais
	elif valor_1 == valor_2:
		#Exibir que os valores são iguais
		print("Os valores se equivalem")
	#Condição onde o segundo número é maior que o primeiro
	else:
		#Exibir o segundo valor como sendo o maior
		print("O maior número é %d" % valor_2)
#Função principal
def main():
	#Variável onde será armazenadoo o primeiro valor fornecido pelo usuário
	valor_1  = int(input("Insira seu primeiro valor: "))
	#Variável onde será armazenadoo o segundo valor fornecido pelo usuário
	valor_2  = int(input("Insira seu segundo valor: "))
	#Chamar a função maior
	maior(valor_1, valor_2)
#Chamar a função principal
main()

