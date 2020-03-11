#7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.
print ("==============================================")
print (" PROGRAMA PARA CALCULAR AREA TOTAL DE UMA CASA")
print ("==============================================")

print("======PRIMEIRO COMODO=========")
largura1 = int(input("Insira o valor da largura em metros: "))
base1 = int(input("Insira o valor da base em metros: "))

print("======SEGUNDO COMODO=========")
largura2  = int(input("Insira o valor da largura em metros: "))
base2 = int(input("Insira o valor da base em metros: "))

print("======TERCEIRO COMODO=========")
largura3 = int(input("Insira o valor da largura em metros: "))
base3 = int(input("Insira o valor da base em metros: "))

print("======QUARTO COMODO=========")
largura4 = int(input("Insira o valor da largura em metros: "))
base4 = int(input("Insira o valor da base em metros: "))

area_total = largura1 * base1 + largura2 * base2 + largura3 * base3 + largura4 * base4

print("Area total e de %dM" % area_total)



