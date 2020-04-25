''' 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
 valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
#Danilo Souza 21/04/2020

#Função note onde será feito o enquanto for verdade com condições
def note(nota):
    #enquanto for verdade
    while True:
        #se nota maior iguala 0 e menor que 0
        if nota >= 0 and nota < 10:
            #exibir valor válido
            print("valor válido")
            #pausar o loop
            break 
        #senão
        else: 
            #exibir valor inválido  
            print("valor inválido")
            #variável nota que vai armazenar um valor fornecido podendo reiniciar o while
            nota = int(input("Informe um valor: "))

#função principal 
def main():
    #variável onde vai ser armazenado um número fornecido pelo usuário 
    nota = int(input("Informe um valor: "))
    #chamar função note(nota)
    note(nota)
#chamar função principal 
main()