'''2 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
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

qt_horas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = 5
INSS = 0.1
FGTS = 0.11
salario_bruto = qt_horas * valor_hora
desconto_FGTS = salario_bruto * FGTS
desconto_INSS = salario_bruto * INSS

#caso1
if salario_bruto <= 900:
	porcetagem_IR1 = 0
	desconto_IR1 = salario_bruto * porcetagem_IR1
	desconto_total1 = desconto_INSS + desconto_IR1
	salarioliquido1 = salario_bruto - desconto_IR1 - desconto_INSS
	print ("salário bruto será de R$%d " % salario_bruto)
	print ("Isento do imposto de renda")
	print ("o valor descontado para o INSS será de R$%d " % desconto_INSS)
	print ("O valor do FGTS será de R$%.2f" % desconto_FGTS)
	print ("Total descontos será de R$%2.f" % desconto_total1)
	print ("O salário liquido será de R$%2.f" % salarioliquido1)
	
#caso2
elif salario_bruto <= 1500:
	porcetagem_IR2 = 0.05
	desconto_IR2 = salario_bruto * porcetagem_IR2
	desconto_total2 = desconto_INSS + desconto_IR2
	salarioliquido2 = salario_bruto - desconto_IR2 - desconto_INSS
	print ("salário bruto será de R$%d " % salario_bruto)
	print ("O desconto do imposto de renda será R$%d " % desconto_IR2)
	print ("o valor descontado para o INSS será de R$%d " % desconto_INSS)
	print ("O valor do FGTS será de R$%.2f" % desconto_FGTS)
	print ("Total descontos será de R$%2.f" % desconto_total2)
	print ("O salário liquido será de R$%2.f" % salarioliquido2)
	
#caso3
elif salario_bruto <= 2500:
	porcetagem_IR3 = 0.1
	desconto_IR3 = salario_bruto * porcetagem_IR3
	desconto_total3 = desconto_INSS + desconto_IR3
	salarioliquido3 = salario_bruto - desconto_IR3 - desconto_INSS
	print ("salário bruto será de R$%d " % salario_bruto)
	print ("O desconto do imposto de renda será R$%d " % desconto_IR3)
	print ("o valor descontado para o INSS será de R$%d " % desconto_INSS)
	print ("O valor do FGTS será de %.2f" % desconto_FGTS)
	print ("Total descontos será de R$%2.f" % desconto_total3)
	print ("O salário liquido será de R$%2.f" % salarioliquido3)
