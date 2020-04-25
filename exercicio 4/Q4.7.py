'''7 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. '''
#DaniloSouza #18/03/2020

#Função onde terá condição para identificar se o ano é bissexto ou não
def year(ano):
	#Se ano tem resto 4 igual e ano com modulo 100 diferente de 0 ou ano modulo 400 é igual 0
	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
		#exibir que o ano é bissexto
		print ("O ano %d é bissexto!!" % ano)
	#Senão 
	else :
		#exibir que o ano não é bissexto
		print ("O ano %d não é bissexto!" % ano )
#função principal
def main():
	#variável que armazena um número disponibilizado pelo usuário
	ano = int(input("Insira o ano que você deseja: "))
	#chamar a função year
	year(ano)
#chamar a função principal 
main()

