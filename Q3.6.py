'''6 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
#DaniloSouza #18/03/2020

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b ** 2 - 4 * a * c
x1 =( - b + (delta ** 0.5) ) / (2 * a)
x2 = (-b - (delta ** 0.5) )/ (2 * a)

print(delta)

if a == 0:
	print ("Esta equação não é de segundo grau. Por favor coloque uma equação válida!")
elif delta <= 0:
	print ("A equação não terá valor real")
elif delta == 0:
	print ("Esta equação possui apenas uma raiz real %d" % delta)
elif delta >= 0:
	print ("Esta equação possui raiz x1: %s" % x1)
	print ("Esta equação possui raiz x2: % s" % x2)
