'''5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
decrescimento iniciais. Valide a entrada e permita repetir a operação'''
#Danilo Souza #21/04/2020


def calc(pA, pB, tA, tB):
    #variável que armazena o ano inicial
    ano = 0
    #enquanto população A for menor iguala população B
    while pA <= pB:
        #pA igual a pA mais tA de pA
        pA = pA + pA * tA / 100
        #pB igual a pB mais tB de pB
        pB = pB + pB * tB / 100
        #cada volta o será adicionado mais 1 ano
        ano = ano + 1

    #exibir o número de anos necessário para se equiparar ou ultrapassar
    print("para população A com a taxa de crescimento %.2f porcento ao ano passar a população B será necessário %d anos" % (tA, ano))

#Função taxa da populacional onde usuário vai fornecer o valor de aumento em porcentagem 
def taxes(pA, pB):
    #variável t1 que armazena o valor da taxa de crescimento anual fornecido pelo usuário
    tA = float(input("Informe a taxa de crescimento: "))
    #variável t1 que armazena o valor da taxa de crescimento anual fornecido pelo usuário
    tB = float(input("Informe a taxa de crescimento: "))
    calc(pA, pB, tA, tB)

#Função população onde será perguntado ao usuário as populações das respectivas cidades
def pop():
    #variável pA(população A) armazenada com 80000 conforme o enunciado
    pA = int(input("Informe a população de A: "))
    #variável pB(população B) armazenada com 200000 conforme o enunciado
    pB = int(input("Informe a população de B: "))
    #chamar a função taxes(pA, pB)
    taxes(pA, pB)
#chamar a função pop
pop()