#1 - Faça um Programa que peça dois números e imprima o maior deles.
#DaniloSouza #14/03/2020


valor_1  = int(input("Insira seu primeiro valor: "))
valor_2  = int(input("Insira seu segundo valor: "))

if valor_1 > valor_2:
	print("O maior número é %d" %valor_1)
elif valor_1 == valor_2:
        print("Os valores se equivalem")
else:
	print("O maior número é %d" %valor_2)

