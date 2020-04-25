'''3 - Em um banho de 5 minutos, fechando o registro ao se ensaboar, 
são gastos 45 litros de água. Sabendo que em 1 m3 de água há 
1.000 litros, calcule quantos banhos de 5 minutos 
são necessários para consumir 1 metro cúbico de água?'''
'DaniloSouza 08/04/2020'
import os 
import sys 

#Função para reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#Função banho
def banho(tempo_banho, Lt_per_minute):
#Calcular a quantidade de litros gastados no banho
    qt_litro = Lt_per_minute * tempo_banho
#Litros consumidos a cada 5 minutos
    Lt_5_minute = Lt_per_minute * 5
#Números de banhos a cada 5 minutos
    num_banho = qt_litro / Lt_5_minute
#Imprimir o número de banhos para o usuário
    print("O número de banhos é %d a cada 5 minutos" % num_banho)
    restart_program()

#função principal.
def main():
    #Duração do banho
    tempo_banho = int(input("Digite o minutos que você demorou para tomar banho em: "))
    #Quantidade de litro por minuto
    Lt_per_minute = int(input("Quantos litros você gastou no banho por minuto: "))
    #Chamar a função banho
    banho(tempo_banho, Lt_per_minute)
#chamar função principal
main()

