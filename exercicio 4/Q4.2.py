'''2 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
#DaniloSouza #18/03/2020

#Função calc onde estão armazenadas algumas variáveis e serão feitos alguns cálculos

def calc(qt_horas, valor_hora):
	#Variável INSS onde armazena o valor fixo de 10%
	INSS = 0.1
	#Variável FGTS onde armazena o valor fixo de 11%
	FGTS = 0.11
	#Salário bruto é igual a quantidade de horas trabalhadas por mês multiplicado pelo valor que a empresa paga por hora
	salario_bruto = qt_horas * valor_hora
	#Desconto do fgts será o salário bruto multiplicado pelo valor FGTS
	desconto_FGTS = salario_bruto * FGTS
	#Desconto do inss será o salário bruto multiplicado pelo valor do inss
	desconto_INSS = salario_bruto * INSS
	liquid_salary(salario_bruto, desconto_INSS, desconto_FGTS)

def liquid_salary(salario_bruto, desconto_INSS, desconto_FGTS):
	#Se o salário bruto for menor igual a 900
	if salario_bruto <= 900:
		#porcetagem de imposto de renda isento
		porcetagem_IR1 = 0
		#valor do desconto do imposto de renda é o salário bruto multiplicado pela porcetagem
		desconto_IR1 = salario_bruto * porcetagem_IR1
		#valor do desconto total é o desconto do INSS somado com o desconto do imposto de renda
		desconto_total1 = desconto_INSS + desconto_IR1
		#Salário liquido será o salário com a dedução dos descontos
		salarioliquido1 = salario_bruto - desconto_IR1 - desconto_INSS
		#exibir o salário bruto
		print("salário bruto será de R$%.2f " % salario_bruto)
		#exibir é isento ao imposto de renda
		print("Isento do imposto de renda")
		#exibir o desconto do inss
		print("o valor descontado para o INSS será de R$%.2f " % desconto_INSS)
		#exibir o desconto do fgts
		print("O valor do FGTS será de R$%.2f" % desconto_FGTS)
		#exibir o desconto total
		print("Total descontos será de R$%.2f" % desconto_total1)
		#exibir o salário liquido
		print("O salário liquido será de R$%.2f" % salarioliquido1)

	#caso2
	#Se salário for menor igual a 1500
	elif salario_bruto <= 1500:
		#Porcetagem de imposto de renda 5%
		porcetagem_IR2 = 0.05
		#valor do desconto do imposto de renda é o salário bruto multiplicado pela porcetagem
		desconto_IR2 = salario_bruto * porcetagem_IR2
		#valor do desconto total é o desconto do INSS somado com o desconto do imposto de renda
		desconto_total2 = desconto_INSS + desconto_IR2
		#Salário liquido será o salário com a dedução dos descontos
		salarioliquido2 = salario_bruto - desconto_IR2 - desconto_INSS
		#Exibir o salário bruto
		print("salário bruto será de R$%d " % salario_bruto)
		#Exibir o desconto do imposto de renda
		print("O desconto do imposto de renda será R$%.2f " % desconto_IR2)
		#exibir o desconto do INSS
		print("o valor descontado para o INSS será de R$%.2f " % desconto_INSS)
		#exibir o valor do FGTS
		print("O valor do FGTS será de R$%.2f" % desconto_FGTS)
		#exibir o desconto total
		print("Total descontos será de R$%.2f" % desconto_total2)
		#exibir o salário liquido
		print("O salário liquido será de R$%.2f" % salarioliquido2)

	#caso3
	#Se salário for menor igual a 2500
	elif salario_bruto <= 2500:
		#porcetagem de imposto de renda 10%
		porcetagem_IR3 = 0.1
		#Desconto do imposto é salário bruto multiplicado pela porcetagem de imposto de renda
		desconto_IR3 = salario_bruto * porcetagem_IR3
		#desconto total é o desconto INSS mais desconto imposto de renda
		desconto_total3 = desconto_INSS + desconto_IR3
		#Salário é o salario bruto com a dedução dos descontos
		salarioliquido3 = salario_bruto - desconto_IR3 - desconto_INSS
		#exibir o salário bruto
		print("salário bruto será de R$%.2f" % salario_bruto)
		#exibir o desconto do imposto de renda
		print("O desconto do imposto de renda será R$%.2f " % desconto_IR3)
		#exibir o desconto do INSS
		print("o valor descontado para o INSS será de R$%.2f " % desconto_INSS)
		#exibir o valor desconto do FGTS
		print("O valor do FGTS será de %.2f" % desconto_FGTS)
		#Exibir o total de descontos
		print("Total descontos será de R$%.2f" % desconto_total3)
		#Exibir o salário liquido
		print("O salário liquido será de R$%.2f" % salarioliquido3)
	#Se o salário bruto for maior que 2500
	elif salario_bruto > 2500:
		#porcetagem de imposto de renda 20%
		porcetagem_IR4 = 0.2
		#Desconto do imposto é salário bruto multiplicado pela porcetagem de imposto de renda
		desconto_IR4 = salario_bruto * porcetagem_IR4
		#desconto total é o desconto INSS mais desconto imposto de renda
		desconto_total4 = desconto_INSS + desconto_IR4
		#Salário é o salario bruto com a dedução dos descontos
		salarioliquido4 = salario_bruto - desconto_IR4 - desconto_INSS
		#exibir o salário bruto
		print("salário bruto será de R$%.2f " % salario_bruto)
		#exibir o desconto do imposto de renda
		print("O desconto do imposto de renda será R$%.2f " % desconto_IR4)
		#exibir o desconto do INSS
		print("o valor descontado para o INSS será de R$%.2f " % desconto_INSS)
		#exibir o valor desconto do FGTS
		print("O valor do FGTS será de %.2f" % desconto_FGTS)
		#Exibir o total de descontos
		print("Total descontos será de R$%.2f" % desconto_total4)
		#Exibir o salário liquido
		print("O salário liquido será de R$%.2f" % salarioliquido4)

#Função principal da aplicação
def main():
	#Variável onde o usuário fornece a quantidade de horas que trabalhou por mês
	qt_horas = int(input("Informe a quantidade de horas trabalhadas: "))
	#Variável onde o usuário fornece o valor que a empresa por cada hora trabalhada
	valor_hora = float(input("Informe o valor pago pela empresa por hora: "))
	#Chamar função calc
	calc(qt_horas, valor_hora)

#Chamar função principal
main()

 
