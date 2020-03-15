#10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
#DaniloSouza #04/03/2020
salario_funcionario = float(input("Informe seu salario atual: "))
percentual_reajuste = float(input("Informe o percentual de reajuste: "))
reajuste = salario_funcionario * percentual_reajuste / 100
novo_salario = salario_funcionario + reajuste
print ("O seu novo salario sera de R$%.2f" % novo_salario)
