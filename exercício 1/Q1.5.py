'''5 - Receba do usuário o ano em que estamos, 
e o ano que ele nasceu, e calcule sua idade.
Despreze os meses.'''
'''Danilo Souza - 08/04/2020'''

#Função para calcular e mostra o resultado da idade do usuário
def idade(usuario_nasc):
#Cálculo da idade do usuário com base no ano atual
    idade_usuario = 2020 - usuario_nasc
#Mostrar na tela o resultado da idade do usuário    
    print("Você está com %d ano(s)" % idade_usuario)
#Função principal
def main():
    #Armazenar dados na variável usuario_nasc
    usuario_nasc = int(input("Informe o ano que você nasceu: "))
    #Chamar a função idade
    idade(usuario_nasc)
#Chamar a função principal
main()

