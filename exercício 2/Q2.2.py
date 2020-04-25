'''Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros
de água. Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos banhos de 5 minutos
são necessários para consumir 1 metro cúbico de água?'''
'''Danilo Souza'''


from sys import executable, argv
from os import execl, system
from time import sleep

def limpa():
    sleep(10)
    system('clear')
    restart_program()
def restart_program():
    python = executable
    execl(python, python, * argv)
def banho(tempo_banho, litro_min):
    consumo = tempo_banho * litro_min
    banho = 1000 / consumo
    print("O número de banho(s) com o tempo de %d minutos para chegar a 1m³ será necessário %.1f banho(s)" % (tempo_banho, banho))
    limpa()
def main():
    tempo_banho = int(input("Quantos minuto(s) você utilizou para tomar banho: "))
    litro_min = int(input("O valor de litro(s) por minuto: "))
    banho(tempo_banho, litro_min)

main()
