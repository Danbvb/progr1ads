'''10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o 
salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).'''
#DaniloSouza #04/03/2020

#Função onde será feito o reajuste salárial
def reajuste(salario_funcionario, percentual_reajuste):
    #Variável onde será feito o cálculo do reajuste salárial.
    reajuste = salario_funcionario * percentual_reajuste / 100
    #Variável onde será feito uma soma do base salário antigo + o reajuste salárial
    novo_salario = salario_funcionario + reajuste
    #Exibir o resultado do novo salário 
    print("O seu novo salario sera de R$%.2f" % novo_salario)
#Função principal
def main():
    #Variável onde será armazenado o valor do salário do funcionário fornecido pelo usuário 
    salario_funcionario = float(input("Informe seu salario atual: "))
    #Variável onde será armazenado o percentual de reajuste  fornecido pelo usuário
    percentual_reajuste = float(input("Informe o percentual de reajuste: "))
    #Chamar a função reajuste
    reajuste(salario_funcionario, percentual_reajuste)
#Chamar a função principal 
main()