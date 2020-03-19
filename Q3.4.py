''' 4 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E. '''
#DaniloSouza #18/03/2020

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
media = (nota1 + nota2)/2
if media > 9 <= 10:
	conceito = "A"
	print ("Sua primeira nota é de %.1f" % nota1)
	print ("Sua segunda nota é de %.1f" % nota2)
	print("Sua média final será de %.1f" % media)
	print ("Seu conceito é de %s" % conceito)
	print ("APROVADO")
elif media >  7.5 <= 9:
	conceito = "B"
	print ("Sua primeira nota é de %.1f" % nota1)
	print ("Sua segunda nota é de %.1f" % nota2)
	print("Sua média final será de %.1f" % media)
	print ("Seu conceito é de %s" % conceito)
	print ("APROVADO")
elif media > 6 <= 7.5:
	conceito = "C"
	print ("Sua primeira nota é de %.1f" % nota1)
	print ("Sua segunda nota é de %.1f" % nota2)
	print("Sua média final será de %.1f" % media)
	print ("Seu conceito é de %s" % conceito)
	print ("APROVADO")
elif media > 4 <= 6:
	conceito = "D"
	print ("Sua primeira nota é de %.1f" % nota1)
	print ("Sua segunda nota é de %.1f" % nota2)
	print("Sua média final será de %.1f" % media)
	print ("Seu conceito é de %s" % conceito)
	print ("REPROVADO")
elif media == 0 < 4:
	conceito = "E"
	print ("Sua primeira nota é de %.1f" % nota1)
	print ("Sua segunda nota é de %.1f" % nota2)
	print("Sua média final será de %.1f" % media)
	print ("Seu conceito é de %s" % conceito)
	print ("REPROVADO")
