''' 5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes; '''
#DaniloSouza #18/03/2020

lado1 = int(input("Qual o valor do lado 1: "))
lado2= int(input("Qual o valor do lado 2: "))
lado3 = int(input("Qual o valor do lado 3: "))

if lado1 + lado2 > lado3:
        if lado1 == lado2 == lado3:
                print ("O triângulo será equilátero porquê todos os lados são iguais!")
        elif lado1 != lado2 != lado3:
                print ("O triângulo será escaleno porquê todos os lados são diferentes!")
        else:
                print ("O triângulo será Isósceles porquê tem dois lados iguais!")
else:
        print ("Não tem os requisitos minimos para se formar um triângulo!")
        print ("Tente novamente respeitando as regras para se formar um triângulo!")
        
