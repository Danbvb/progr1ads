'''3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

#Função nome saberá se o nome está apto ou não
def name(nome):
    #enquanto for verdade
    while True:
        #n recebe a quantidade de letras na variável nome
        n = len(nome)
        #se n for maior que 3
        if n > 3:
            #Exibir nome válido
            print("Nome válido")
            #parar o loop
            break
        #senão
        else:
            #exibir nome inválido
            print("nome inválido")
            #repete a variável nome e criar um looping até o funcionário receber o nome certo
            nome = input("informe seu nome: ")
#função salário onde terá as condições para saber se o salário está apto ou não
def salary(salario):
    #enquanto for verdade
    while True:
        #se salário for maior que 0
        if salario > 0:
            #exibir salário válido
            print("Salário válido")
            #parar o looping
            break
        #senão
        else:
            #exibir salário inválido
            print("Salário inválido")
            #repete a variável salário até o usuário informar um valor apto
            salario = int(input("Informe seu salário: "))
#função sex onde terá as condições para saber se está apto ou não
def sex(sexo):
    #enquanto for verdade
    while True:
        #se sexo for igual a m ou f
        if sexo == "m" or sexo == "f":
            #exibir sexo válido
            print("sexo válido")
            #parar o looping
            break
        #senão
        else:
            #exibir sexo inválido
            print("sexo inválido")
            #repetir a variável até o usuário inserir uma letra válida
            sexo = input("Informe seu sexo: ")
#função ec para saber se o estado civil do usuário está apto ou não
def ec(estado_civil):
    #enquanto for verdade
    while True:
        #se estado civil for c, s, v, d
        if estado_civil == "c" or estado_civil == "s" or estado_civil == "v" or estado_civil == "d":
            #exibir apto
            print("Apto")
            #parar o looping
            break
        #senão
        else:
            #exibir não apto
            print("Não apto")
            #repetir a variável estado civil até o usuário fornecer uma letra apta
            estado_civil = input("Informe o seu estado civil: ")

#função principal
def main():
    #variável onde o usuário vai fornecer seu nome
    nome = input("Informe o seu nome: ")
    #chamar a função name(nome)
    name(nome)
    #variável onde o usuário vai fornecer seu salário
    salario = int(input("Informe o seu salário: "))
    #chamar a função salary(salario)
    salary(salario)
    #variável onde o usuário vai fornecer seu sexo
    sexo = input("informe o seu sexo: ")
    #chamar a função sex(sexo)
    sex(sexo)
    #variável onde o usuário vai fornecer estado civil
    estado_civil = input("infome o seu estado civil: ")
    #chamar a ec(estado_civil)
    ec(estado_civil)

#chamar função principal   
main()
