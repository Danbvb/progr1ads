'''4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
#DaniloSouza #14/03/2020

#Função onde terá as condições para saber se a letra fornecida pelo usuário é uma vogal ou consoante
def letter(letra):
	#Condição caso a letra seja uma vogal minúscula 
	if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
		#Exibir que a letra é uma vogal
		print("Essa letra é uma vogal")
	#Condição caso a letra seja uma vogal maiúscula 
	elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
		#Exibir que a letra é uma vogal
		print("Essa letra é uma vogal!")
	#Condição caso a letra não seja uma vogal maiúscula ou minúscula
	else:
		#Exibir que a letra é uma consoante
		print("Essa letra é uma consoante!")

#função principal
def main():
	#Variável onde será armazenado a letra fornecida pelo usuário
	letra = input("Insira a letra desejada: ")
	#chamar função letter
	letter(letra)
#chamar a função principal 
main()


