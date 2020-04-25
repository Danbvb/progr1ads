''' 5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes; '''
#DaniloSouza #18/03/2020

#Função onde terá as condições para identificar o triângulo
def triangule(lado1, lado2, lado3):
	#Se todos os lados forem iguais
	if lado1 == lado2 == lado3:
		#Exibir que será o triângulo equilátero
		print("O triângulo será equilátero porquê todos os lados são iguais!")
	#Se todos os lados forem diferentes
	elif lado1 != lado2 != lado3:
		#Exibir que será triângulo escaleno
		print("O triângulo será escaleno porquê todos os lados são diferentes!")
	#Senão
	else:
		#Exibir que será um triângulo isósceles
		print("O triângulo será Isósceles porquê tem dois lados iguais!")

#Função principal
def main():
	#Variável onde será armazenado o valor do lado 1
	lado1 = int(input("Qual o valor do lado 1: "))
	#Variável onde será armazenado o valor do lado 2
	lado2= int(input("Qual o valor do lado 2: "))
	#Variável onde será armazenado o valor do lado 3
	lado3 = int(input("Qual o valor do lado 3: "))
	#chamar função triangule
	triangule(lado1, lado2, lado3)

#chamar função principal
main()

