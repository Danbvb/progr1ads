#3. Faça um programa que calcule a média de consumo de combustível de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

Km_inicial = int(input("Insira o valor da distancia inicial: "))
Km_final = int(input("Insira o valor da distancia final: "))
consumo = int(input("Quantos litros de combustivel foram gastos durante o percurso: "))
media = ( Km_final - Km_inicial) / consumo
print ("A media de consumo de combustivel sera de %.fKm por Lt." % media)
