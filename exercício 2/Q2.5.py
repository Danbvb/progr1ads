'''#5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O 
usuário deve informar o valor original da dívida (ex. R$ 50,00),  a quantidade de
dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).'''
#DaniloSouza #11/03/2020 

#Função onde terá condições que dependendo da quantidade de dias no atraso o valor diária da multa.
def bill(vlr_inicial, dias_de_atraso):
    #Condição onde o atraso do pagamento do usuário está abaixo dos 10 dias.
    if dias_de_atraso <= 10:
        #Valor diário da multa até o 10 dias.
        multa_diaria = 0.15
    #Condição onde o atraso do pagamento do usuário está acima dos 10 dias e abaixo dos 20 dias.
    elif dias_de_atraso > 10 and  dias_de_atraso <= 20:
        #Valor diário da multa maior que 10 dias e menor que 20 dias.
        multa_diaria = 0.20
    #Condição onde o atraso do pagamento do usuário está acima dos 20 dias e abaixo dos 30 dias.
    elif dias_de_atraso > 20 and dias_de_atraso <= 30:
        #Valor diário da multa maior que 20 dias e menor que 30 dias.
        multa_diaria = 0.25
    #Condição onde o atraso do pagamento do usuário está acima dos 30 dias.
    elif dias_de_atraso > 30:
        #Valor diário da multa maior que 30 dias
        multa_diaria = 0.30
    #Variável onde será feito o cálculo da dívida de atraso.
    valor_final = multa_diaria * dias_de_atraso + vlr_inicial
    #Exibir o novo valor dívida com a adição da multa diária.
    print("O valor da divida R$%d inicial com %d dias de atraso terá adição de R$%.2f ficando R$%.2f" % (vlr_inicial, dias_de_atraso, multa_diaria, valor_final))
'''
def choose_payment(valor_final):
'''  
#Função principal da aplicação.  
def main():
    #Variável onde será armazenado o valor original da dívida fornecido pelo usuário.
    vlr_inicial = int(input("Insira o valor original: "))
    #Variável onde será armazenado a quantidade de dias em atraso fornecido pelo usuário.
    dias_de_atraso = int(input("Insira a quantidade de dias em atrasos: "))
    #Chamar a função Bill
    bill(vlr_inicial, dias_de_atraso)
    
#Chamar a função principal da aplicação
main()