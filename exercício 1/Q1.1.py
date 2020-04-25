''' 1 - Escreva um programa que recebe o nome do usuário e, em seguida,
 imprime a frase Olá, nome_do_usuário!. '''
 'Danilo Souza 08/04/2020'

#Variável onde armazenará o nome do usuário
usuario = input('insira seu nome: ')

#Função de texto onde mostrará o fim do programa
def title(titulo):
    #Exibir 10 - 
    print('-' * 10)
    #Exibir a variável titulo
    print(titulo)
    #Exibir 10 -
    print('-' * 10)

#Chamar a função title onde está armazenado o nome do usuário.
title('Olá, %s!' % usuario)

