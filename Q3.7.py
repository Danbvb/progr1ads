'''7 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. '''
#DaniloSouza #18/03/2020

ano = int(input("Insira o ano que você deseja: "))

if ano % 4 == 0 and ano % 100 != 0 or ano  == 400:
	print ("O ano %d é bissexto!!" % ano)
else :
	print ("O ano %d não é bissexto!" % ano )
