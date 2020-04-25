''' 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senhaigual
 ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir asinformações.'''
 #Danilo Souza 21/04/2020

#função login onde o enquanto e as condições para saber se é verdade
def login(usuario, senha):
    #enquanto for verdade
    while True:
        #se usuário for igual a senha
        if usuario == senha:
            #exibir login inválido
            print("login inválido")
            #chamar função principal 
            usuario = input("informe o nome do usuário: ")
            #variável que recebe uma senha fornecido pelo usuário
            senha = input("informe uma senha: ")
        #senão
        else:
            #exibir login aceito 
            print("login aceito")
            #parar o loop
            break
#função principal 
def main(): 
    #variável que recebe um nome fornecido pelo usuário
    usuario = input("informe o nome do usuário: ")
    #variável que recebe uma senha fornecido pelo usuário
    senha = input("informe uma senha: ")
    #chamar função login(usuario, senha)
    login(usuario, senha)
#chamar função principal
main()
