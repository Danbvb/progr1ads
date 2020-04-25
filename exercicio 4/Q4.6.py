'''6 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
#DaniloSouza #18/03/2020

#importar a função sqrt da biblioteca math
from math import sqrt

#Função onde será feito a formula de bhaskara 
def d(a, b, c):
	#retornar o valor de delta
	return b ** 2 - 4 * a * c

#Funções onde estarão as condições para prosseguir o cálculo
def conditions(d, a, b, c):
	#Variável delta para armazenar o valor de bhaskara
	delta = d
	#Se delta for menor que 0
	if delta < 0:
		#Exibir que a equação não terá valor real
		print ("A equação não terá valor real")
	#Se delta for igual a 0
	elif delta == 0:
		#Exibir que a equação possui um valor real
		print ("Esta equação possui apenas uma raiz real %d" % delta)
	#Se delta maior igual a 0
	elif delta >= 0:
		#variável x1 armazena a formúla para encontrar a raiz de x1
		x1 = - b + sqrt(delta) / (2 * a)
		#variável x1 armazena a formúla para encontrar a raiz de x2
		x2 = - b - sqrt(delta) / (2 * a)
		#Exibir a raiz x1
		print ("Esta equação possui raiz x1: %s" % x1)
		#Exibir a raiz x2
		print ("Esta equação possui raiz x2: %s" % x2)

#função principal 
def main():
	#variável que armazena valor de a fornecido pelo usuário
	a = int(input("Informe o valor de a: "))
	#variável que armazena valor de b fornecido pelo usuário
	b = int(input("Informe o valor de b: "))
	#variável que armazena valor de c fornecido pelo usuário
	c = int(input("Informe o valor de c: "))
	#Se a for igual a 0
	if a == 0:
		#Exibir que a equação não é de segundo grau
		print("Esta equação não é de segundo grau. Por favor coloque uma equação válida!")
	#Senão
	else:
		#chamar função d
		d(a, b, c)
		#chamar função conditions
		conditions(d, a, b, c)
#chamar função principal 
main()
