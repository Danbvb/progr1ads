'''8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
'''Danilo Souza 14/03/2020'''

produto1 = float(input("Informe o valor do primeiro produto: "))
produto2 = float(input("Informe o valor do segundo produto: "))
produto3 = float(input("Informe o valor do terceiro produto: "))
moeda = str(input("Informe a moeda que você irá utilizar para comprar o produto: "))

if produto1 < produto2 and produto3:
	print("O produto mais barato é o primeiro produto com o valor de %.2f em %s" % (produto1, moeda))
elif produto2 < produto1 and produto3:
	print("O produto mais barato é o segundo produto com o valor de %.2f em %s" % (produto2, moeda))
elif produto3 < produto1 and produto2:
	print("O produto mais barato é o terceiro produto com o valor de %.2f em %s" % (produto3, moeda))

