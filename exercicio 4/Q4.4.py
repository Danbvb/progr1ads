''' 4 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E. '''
#DaniloSouza #18/03/2020

#Função onde será feita a média aritmética
def m(nota1, nota2):
	#retornar para função m o valor da média aritmética
	return (nota1 + nota2)/2
#Função onde terá as condições para saber a nota final do aluno.
def media(nota1, nota2):
	#media vai armazenar o retorno da m
	media = m(nota1, nota2)
	#se a média for maior que 9 e menor igual a 10
	if media > 9 <= 10:
		#variável onde será armazenado o conceito
		conceito = "A"
		#exibir a primeira nota
		print ("Sua primeira nota é de %.1f" % nota1)
		#exibir a segunda nota
		print ("Sua segunda nota é de %.1f" % nota2)
		#exibir a média final
		print("Sua média final será de %.1f" % media)
		#exibir o conceito 
		print ("Seu conceito é de %s" % conceito)
		#exibir que está aprovado
		print ("APROVADO")
	#se media for maior que 7.5 e menor igual a 9
	elif media > 7.5 <= 9:
		#variável armazena o conceito
		conceito = "B"
		#exibir a primeira nota
		print ("Sua primeira nota é de %.1f" % nota1)
		#exibir a segunda nota
		print ("Sua segunda nota é de %.1f" % nota2)
		#exibir a média final
		print("Sua média final será de %.1f" % media)
		#exibir o conceito 
		print ("Seu conceito é de %s" % conceito)
		#exibir aprovado
		print ("APROVADO")
	#Se media for maior que 6 e menor igual a 7.5
	elif media > 6 <= 7.5:
		#variável que armazena o conceito
		conceito = "C"
		#exibir a primeira nota
		print ("Sua primeira nota é de %.1f" % nota1)
		#exibir a segunda nota
		print ("Sua segunda nota é de %.1f" % nota2)
		#exibir a média final
		print("Sua média final será de %.1f" % media)
		#exibir o conceito
		print ("Seu conceito é de %s" % conceito)
		#exibir aprovado
		print ("APROVADO")
	#se media for maior que 4 e menor igual a 6
	elif media > 4 <= 6:
		#variável onde armazena o conceito
		conceito = "D"
		#exibir a primeira nota
		print ("Sua primeira nota é de %.1f" % nota1)
		#exibr a segunda nota
		print ("Sua segunda nota é de %.1f" % nota2)
		#exibir a média final
		print("Sua média final será de %.1f" % media)
		#exibir o conceito
		print ("Seu conceito é de %s" % conceito)
		#exibir reprovado
		print ("REPROVADO")
	#se media for igual a 0 e mnor que 4 
	elif media == 0 < 4:
		#variável que armazena o conceito
		conceito = "E"
		#exibir a primeira nota
		print ("Sua primeira nota é de %.1f" % nota1)
		#exibir a segunda nota 
		print ("Sua segunda nota é de %.1f" % nota2)
		#exibir a media final
		print("Sua média final será de %.1f" % media)
		#exibir o conceito
		print ("Seu conceito é de %s" % conceito)
		#exibir reprovado
		print ("REPROVADO")

#Função principal
def main():
	#Variável onde será armazenado o valor da primeira nota fornecido pelo usuário
	nota1 = float(input("Insira sua primeira nota: "))
	#Variável onde será armazenado o valor da segunda nota fornecido pelo usuário
	nota2 = float(input("Insira sua segunda nota: "))
	#chamar a função m
	m(nota1, nota2)
	#chamar a função media
	media(nota1, nota2)

#chamar função principal
main()