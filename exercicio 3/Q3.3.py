'''3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
#DaniloSouza #14/03/2020

#Função onde terá as condições para verificar o gênero fornecido pelo usuário.
def genre(genero):
	#Condição para caso a resposta for F ou f para feminino
	if genero == "F" or genero == "f":
		#Exibir que o gênero fornecido é feminino 
		print ("Seu gênero é feminino!")
	#Condição para caso a resposta for M ou m para masculino
	elif genero == "M" or genero == "m":
		#Exibir que o gênero é masculino
		print ("Seu gênero é masculino!")
	#Condição onde a resposta não é feminino ou masculino
	else:
		#Exibir que o gênero é inválido.
		print ("Gênero inválido!")

#Função principal 
def main():
	#Variável onde vai armazenar a letra em que o usuário for digitar
	genero = str(input("Qual é o seu gênero: "))
	#Chamar a função genre
	genre(genero)

#chamar a função principal 
main()