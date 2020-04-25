'''4 - Escreva um programa que leia uma temperatura em graus Fahrenheit, 
transforme-a em graus Celsius e exiba o resultado.'''
#DaniloSouza #11/03/2020

#Função onde será executada a conversão desejada pelo usuário.
def temp(choose):
    #Condição que deve ser seguida se a escolha do usuário for Celsius.
    if choose == "C":
        #Variável onde pedirá o valor no qual usuário quer converter em Fahrenheit para Celsius.
        F = float(input("Insira a temperatura em fahrenheit: "))
        #Variável onde aprensenta a fórmula de conversão de ºF para ºC 
        C = ( F - 32 ) * 5 / 9
        #Exibir o resultado da conversão em Celsius.
        print ("A temperatura em Celsius será de %.2f" % C)

    #Condição que deve ser seguida se a escolha do usuário for Fahrenheit.
    elif choose == "F":
        #Variável onde pedirá o valor no qual usuário quer converter em Celsius para Fahrenheit para Celsius.
        C = float(input("Insira a temperatura em celsius: "))
        #Variável onde apresenta a fórmula de conversão de ºC para ºF.
        F = (C * 9 / 5) + 32
        #Exibir o resultado da conversão em Fahrenheit.
        print("A tempuratura em Fahrenheit será de %.2f" % F)
    else:
        #Exibir que a letra que foi digitada na variável choose está inválida.
        print("Letra para conversão inválida!")

#Função principal da aplicação onde será perguntado a unidade temperatura desejada para conversão.
def main():
    #Variável onde irá ler a letra que representa a unidade desejada
    choose = input("Informe a sua conversão desejada: ")
    #Chamar a função temp(choose) onde será feita a conversão.
    temp(choose)
#Chamar a função principal da aplicação.
main()
