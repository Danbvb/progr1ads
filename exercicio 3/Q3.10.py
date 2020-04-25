'''10 - Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
"Valor Inválido!", conforme o caso.'''
'''DaniloSouza 14/03/2020'''

#Função onde terá as condições para definir o turno 
def turn(turno_estudo):
	#Se o turno de estudo for igual a M
	if turno_estudo == "M" and turno_estudo == "m":
		#Exibir bom dia
		print("Bom dia!")
	#Se o turno de estudo for igual a V
	elif turno_estudo == "V" and turno_estudo == "v":
		#Exibir boa tarde
		print("Boa tarde!")
	#Se o turno de estudo for igual a N
	elif turno_estudo == "N" and turno_estudo == "n":
		#Exibir boa noite
		print("Boa noite!")
	#Senão
	else:
		#Exibir valor inválido
		print("Valor inválido")

#Função principal 
def main():
	#Variável que armazena o turno de estudo fornecido pelo usuário
	turno_estudo = input("Qual é o turno que você estuda: ")
	#Chamar função turn
	turn(turno_estudo)
	
#Chamar função principal 
main()