''' 3 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''
#DaniloSouza #18/03/2020

#Função onde terá as condições para definir o dia na semana 
def day_a_week(numero):
        #Se o dia da semana for igual a 1
        if numero == 1:
                #exibir que o número corresponde a domingo
                print ("Esse número corresponde ao domingo")
        #Se o dia da semana for igual a 2
        elif numero == 2:
                #Exibir que o número corresponde a segunda-feira
                print ("Esse número corresponde a segunda-feira")
        #Se o dia da semana for igual a 3
        elif numero == 3:
                #Exibir que o número corresponde a terça-feira
                print ("Esse número corresponde a terça-feira")

        #Se o dia da semana for igual a 4
        elif numero == 4:
                #Exibir que o número corresponde a quarta-feira
                print ("Esse número corresponde a quarta-feira")
        #Se o dia da semana for igual a 5
        elif numero == 5:
                #Exibir que o número corresponde a quinta-feira
                print ("Esse número corresponde a quinta-feira")
        #Se o dia da semana for igual a 6
        elif numero == 6:
                #Exibir que o número corresponde a sexta-feira
                print ("Esse número corresponde a sexta-feira")
        #Se o dia da semana for igual a 7
        elif numero == 7:
                #Exibir que o número corresponde a sábado
                print ("Esse número corresponde a sábado")
        #Senão
        else:
                #Exibir número inválido
                print ("número inválido!")

#função principal
def main ():
        #Variável onde será armazenada o número fornecido pelo usuário
        numero = int(input("Insira um número desejado: "))
        #chamar a função day_a_week
        day_a_week(numero)
#chamar a função principal 
main()

