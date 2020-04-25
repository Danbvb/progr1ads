'''

10 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
#DaniloSouza #18/03/2020

#função calc onde será calculado a média aritmética
def	calc(nota1, nota2, nota3):
	#retornar o resultado da função
	return (nota1 + nota2 + nota3) / 3
#função onde tem as condições para saber se o aluno foi aprovado ou não
def media(nota1, nota2, nota3, calc):
	#variável feita para armazena o resultado da função calc
	media = calc(nota1, nota2, nota3)
	#Se media for igual a 10
	if media == 10:
		#Exibir  aprovado com distinção 
		print ("Parabéns, você foi aprovado com distinção")
	#Se media for maior igual a 7
	elif media >= 7:
		#Exibir aprovado
		print ("Parábens, você foi aprovado")
	#se a media for menor igual a 7
	elif media < 7:
		#exibir reprovado
		print("Você foi reprovado, tente novamente no próximo semestre")
	
#função principal
def main():
	#variável que armazena primeira nota fornecido pelo usuário 
	nota1 = float(input("Insira sua primeira nota: "))
	#variável que armazena segunda nota fornecido pelo usuário
	nota2 = float(input("Insira sua segunda nota: "))
	#variável que armazena terceira nota fornecido pelo usuário
	nota3 = float(input("Insira sua terceira nota: "))
	#chamar função calc
	calc(nota1, nota2, nota3)
	#chamar função media
	media(nota1, nota2, nota3, calc)
#chamar função principal 
main()
