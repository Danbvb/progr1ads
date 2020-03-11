#10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario_funcionario = int(input("Informe seu salario atual: "))
reajuste = salario_funcionario * 13.5 / 100
novo_salario = salario_funcionario + reajuste
print ("O seu novo salario sera de R$%.2f" % novo_salario)
