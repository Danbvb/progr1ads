'''2 - Sabendo que a cotação atual do dólar americano é R$ 4,47, receba um valor em reais do usuário e converta para dólares. Exemplo de saída: $ 1.00'''

#Função feita para efetuar o cálculo da conversão de real parar dólar e mostra o resultado final.
def realtodolar(usuario_valor, dolar):
        #Cálculo feito para converter o valor em BRL para USD.
        conversao = dolar / usuario_valor
        #Imprimir o resultado conversão.
        print('$%.2f' % conversao)      
#Função principal
def main():
    #variavel utilizada para ler o valor no qual o usuário coloca em BRL.
    usuario_valor = float(input("Insira o valor em reais: "))
    #variavel utilizada para ler a cotação do dólar americano.
    dolar = float(input("Valor do dólar hoje: "))   
    #chamar função realtodolar
    realtodolar(usuario_valor, dolar)
#Chamar função principal
main()