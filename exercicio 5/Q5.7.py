'''7 - Faça um programa que leia 5 números e informe o maior número'''

#number recebe o valor de 0 que é elemento neutro da soma 
number = 0
#para number no alcance de até 5 
for number in range(5):
    #variável recebe um número digitado pelo usuário
    n = int(input("informe um número: "))
    #se n for maior que number
    if n > number:
        #number recebe n 
        number = n 

#exibir number 
print('o maior número será o %d' % number)