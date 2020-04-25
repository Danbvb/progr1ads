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


#Os números são utilizados para diferenciar cada variavél representando cada caso na questão

#Função salary onde será efetuado o aumento do salário com base no fornecimento do usuário
def salary(salario_atual):
	#Se o salário atual for menor igual a 280   
	if salario_atual <= 280:
		#porcetagem de aumento de 20%
		porcetagem1 = 0.2
		#Valor do aumento do salário multiplicado pela porcetagem
		valor_aumento1 = salario_atual * porcetagem1
		#Novo salário após ter somado o salário antes do reajust + valor de aumento
		novo_salario1 = salario_atual + valor_aumento1
		#Exibir o salário antes do reajuste
		print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
		#Exibir a porcetagem de aumento
		print ("A porcetagem de aumento será de %.2f " % porcetagem1)
		#Exibir o valor do aumento
		print ("O valor do aumento será de R$%.2f" % valor_aumento1)
		#Exibir o novo saláro
		print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario1)
		
		#Se salário atual for menor igual a 700
	elif salario_atual <= 700:
		#Porcetagem de aumento 15%
		porcetagem2 = 0.15
		#Valor do aumento do salário multiplicado pela porcetagem
		valor_aumento2 = salario_atual * porcetagem2
		#Novo salário após ter somado o salário antes do reajust + valor de aumento
		novo_salario2 = salario_atual + valor_aumento2
		#Exibir o salário antes do reajuste
		print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
		#Exibir a porcetagem de aumento
		print ("A porcetagem de aumento será de %.2f " % porcetagem2)
		#Exibir o valor de aumento
		print ("O valor do aumento será de R$%.2f" % valor_aumento2)
		#Exibir o novo salário 
		print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario2)
	
	#Se o salário atual for menor igual a 1500
	elif salario_atual <= 1500:
		#Porcetagem de aumento 10%
		porcetagem3 = 0.1
		#Valor do aumento do salário atual multiplicado pela porcetagem
		valor_aumento3 = salario_atual * porcetagem3
		#Novo salário sendo adição do salário atual + valor de aumento
		novo_salario3 = salario_atual + valor_aumento3
		#Exibir o salário antes do reajuste
		print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
		#Exibir a porcetagem de aumento
		print ("A porcetagem de aumento será de %.2f " % porcetagem3)
		#Exibir o valor do aumento
		print ("O valor do aumento será de R$%.2f" % valor_aumento3)
		#Exibir o novo salário
		print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario3)
	
	#Se salário atual for maior que 1500
	elif salario_atual > 1500:
		#Porcetagem de aumento 5%
		porcetagem4 = 0.05
		#Valor de aumento será salário atual multiplicado pela porcetagem
		valor_aumento4 = salario_atual * porcetagem4
		#novo salário será salário atual somado com o valor de aumento 
		novo_salario4 = salario_atual + valor_aumento4
		#Exibir o valor do salário
		print ("o valor do salário antes do reajuste é de R$%d" % salario_atual)
		#Exibir a porcetagem de aumento
		print ("A porcetagem de aumento será de %.2f " % porcetagem4)
		#Exibir o valor de aumento
		print ("O valor do aumento será de R$%.2f" % valor_aumento4)
		#Exibir o novo salário
		print ("O novo salário após o aumento aplicado será de R$%d" % novo_salario4)


def main():
	#variável criada para informar o salário atual do usuário
	salario_atual = int(input("Informe seu salário atual: "))
	#Chamar a função salary
	salary(salario_atual)

#chamar a função principal
main()	

