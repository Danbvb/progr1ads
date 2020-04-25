'''3. Faça um programa que calcule a média de consumo de combustível de um veículo.
 O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km)
  e quantos litros foram gastos no percurso. 
  Danilo Souza - 17/04/2020
'''
#Função onde será feito o cálculo da média de consumo do combustível
def calc(Km_inicial, Km_final, consumo):
    #Cálculo da média onde será feito a partir da distância final substraindo a inicial dividida pelo consumo de gasolina
    media = (Km_final - Km_inicial) / consumo
    #Exibir o resultado da média de consumo da gasolina por Km e finalizará a aplicação.
    print("A media de consumo de combustivel sera de %.2fKm por Lt." % media)

#Função Principal da aplicação
def main():
    #Variável que irá armazenar o valor da distância inicial
    Km_inicial = int(input("Insira o valor da distancia inicial: "))
    #Variável que irá armazenar o valor da distância final
    Km_final = int(input("Insira o valor da distancia final: "))
    #Variável que irá armazenar a quantidade de gasolina usada durante todo o trajeto.
    consumo = int(input("Quantos litros de combustivel foram gastos durante o percurso: "))
    #Chamar a função calc
    calc(Km_inicial, Km_final, consumo)
main()