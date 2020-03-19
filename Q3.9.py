'''9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
#DaniloSouza #18/03/2020

numero = int(input("Insira o número até 1000: "))
unidade = numero // 1 % 10 
dezena = numero // 10 % 10
centena = numero // 100 % 10
if numero < 10 :
	print("%d = %d unidades" % (numero, unidade))
if numero >= 10 and numero < 100:
	print("%d = %d dezenas e %d unidades" % (numero, dezena, unidade))
elif numero >= 100 and numero <1000:
	print ("%d = %d centenas, %d dezenas e %d unidades" % (numero, centena, dezena, unidade))
else:
	print ("Número inválido! Por favor digite um número até 1000!")
