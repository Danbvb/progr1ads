'''

10 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
#DaniloSouza #18/03/2020

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
nota3 = float(input("Insira sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
	print ("Parabéns, você foi aprovado com distinção")
elif media >= 7:
	print ("Parábens, você foi aprovado")
elif media < 7:
	print("Você foi reprovado, tente novamente no próximo semestre")