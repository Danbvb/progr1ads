'''11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-- caso1 - salários até R$ 280,00 (incluindo) : aumento de 20%
-- caso2 - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- caso3 - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- caso4 - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.
'''
#DaniloSouza #18/03/2020

#variável criada para informar o salário atual
salario_atual = int(input("Informe seu salário atual: "))

#Os números são utilizados para diferenciar cada variavél representando cada caso na questão
                    
if salario_atual <= 280:
	porcetagem1 = 0.2
	valor_aumento1 = salario_atual * porcetagem1
	novo_salario1 = salario_atual + valor_aumento1
	print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
	print ("A porcetagem de aumento será de %.2f " % porcetagem1)
	print ("O valor do aumento será de R$%.2f" % valor_aumento1)
	print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario1)

elif salario_atual <= 700:
	porcetagem2 = 0.15
	valor_aumento2 = salario_atual * porcetagem2
	novo_salario2 = salario_atual + valor_aumento2
	print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
	print ("A porcetagem de aumento será de %.2f " % porcetagem2)
	print ("O valor do aumento será de R$%.2f" % valor_aumento2)
	print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario2)
	
elif salario_atual <= 1500:
	porcetagem3 = 0.1
	valor_aumento3 = salario_atual * porcetagem3
	novo_salario3 = salario_atual + valor_aumento3
	print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
	print ("A porcetagem de aumento será de %.2f " % porcetagem3)
	print ("O valor do aumento será de R$%.2f" % valor_aumento3)
	print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario3)
elif salario_atual > 1500:
	porcetagem4 = 0.05
	valor_aumento4 = salario_atual * porcetagem4
	novo_salario4 = salario_atual + valor_aumento4
	print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
	print ("A porcetagem de aumento será de %.2f " % porcetagem4)
	print ("O valor do aumento será de R$%.2f" % valor_aumento4)
	print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario4)	

