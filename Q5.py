#5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
#DaniloSouza #11/03/2020 
valor_original = int(input("Insira o valor original: "))
dias_de_atraso = int(input("Insira a quantidade de dias em atrasos: "))
multa_diaria = 0.25
valor_final = 0.25 * dias_de_atraso + valor_original
print ("O valor da divida com reajuste sera de %.2f" % valor_final)

