'''9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
 dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
#DaniloSouza #18/03/2020

#função unidade onde será feito a cálculo da unidade 
def unidade(numero):
	#retorna a unidade  
	return numero // 1 % 10
#função dezena onde será feito o cálculo da dezena
def dezena(numero):
	#retorna a dezena
	return numero // 10 % 10
#função centena onde será feito o cálculo da centena
def centena(numero):
	return numero // 100 % 10
#função numbers onde tem condições para saber quantas centenas, unidades ou centenas 
def numbers(numero, unidade, dezena, centena):
	#armazena o retorno da variável unidade
	u = unidade(numero)
	#armazena o retorno da variável dezena
	d = dezena(numero)
	#armazena o retorno da variável centena
	c = centena(numero)
	#se numero for menor que 10
	if numero < 10 :
		#Exibir o número digitado pelo usuário e quantidade de unidade(s)
		print("%d = %d unidades" % (numero, u))
	#se numero for maior igual a 10 e menor que 100
	elif numero >= 10 and numero < 100:
		#Exibir o número digitado pelo usuário, quantidade de unidade(s) e dezena(s)
		print("%d = %d dezenas e %d unidades" % (numero, d, u))
	#se o número for maior igual a 100 e menor que 1000
	elif numero >= 100 and numero <1000:
		#exibir o número digitado pelo usuário, quantidade unidade(s), dezena(s) e centena(s)
		print ("%d = %d centenas, %d dezenas e %d unidades" % (numero, c, d, u))
	#senão
	else:
		#exibir que o número inválido.
		print("Número inválido! Por favor digite um número até 1000!")

#Função principal 
def main():
	#Variável armazena o número fornecido pelo usuário
	numero = int(input("Insira o número até 1000: "))
	#chamar função unidade
	unidade(numero)
	#chamar função dezena
	dezena(numero)
	#chamar função centena
	centena(numero)
	#chamar função numbers
	numbers(numero, unidade, dezena, centena)

#chamar função principal
main()
