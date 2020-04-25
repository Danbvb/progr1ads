'''Suponha que a população de um país A seja da ordem de 80.000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com 
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.'''

#variável pA(população A) armazenada com 80000 conforme o enunciado 
pA = 80000
#variável pB(população B) armazenada com 200000 conforme o enunciado
pB = 200000
#variável que armazena o ano inicial
ano = 0

#enquanto população A for menor iguala população B
while pA <= pB:
    #pA igual a pA mais 3% de pA
    pA = pA + pA * 0.03
    #pB igual a pB mais 3% de pB
    pB = pB + pB * 0.015
    #cada volta o será adicionado mais 1 ano
    ano = ano + 1
    
#exibir o número de anos necessário para se equiparar ou ultrapassar 
print("para população A com a taxa de crescimento 0.03 ao    ano passar a população B será necessário %d anos" % ano)
    
