'''5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
#DaniloSouza #14/03/2020

#Função média o será feito a média aritmética e as condições para saber se o aluno aprovado ou reprovado
def media(media1, media2):
	#Formúla da média aritmética onde irá somar os valores armazenados nas variáveis e dividir pela quantidade de notas.
	mediaf = (media1 + media2)/
	#Se a média final for igual a 10
	if mediaf == 10:
	#Exibir aprovado com distinção
		print("Aprovado com Distinção!")
	#Se a média for maior ou igual a 7
	elif mediaf >= 7:
		#Exibir aprovado
		print("Aprovado!")
	#Se a média for menor ou igual a 6.9
	elif mediaf <= 6.9:
		#Exibir reprovado
		print("Reprovado!")

#Função principal
def main():
	#Variável onde vai armazenar a primeira nota fornecida pelo usuário.
	media1 = float(input("Insira sua primeira nota: "))
	#Variável onde vai armazenar a segunda nota fornecida pelo usuário.
	media2 = float(input("Insira sua segunda nota: "))
	#chamar função media
	media(media1, media2)

#chamar a função principal
main()


