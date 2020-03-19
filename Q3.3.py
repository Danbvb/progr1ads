''' 3 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''
#DaniloSouza #18/03/2020

numero = int(input("insira um número desejado: "))
if numero == 1:
        print ("Esse número corresponde ao domingo")
elif numero == 2:
        print ("Esse número corresponde a segunda-feira")
elif numero == 3:
        print ("Esse número corresponde a terça-feira")
elif numero == 4:
        print ("Esse número corresponde a quarta-feira")
elif numero == 5:
        print ("Esse número corresponde a quinta-feira")
elif numero == 6:
        print ("Esse número corresponde a sexta-feira")
elif numero == 7:
        print ("Esse número corresponde a sábado")
else:
        print ("número inválido!")
        print ("por favor, insira outro número")
