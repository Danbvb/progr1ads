'''4 - Calcule a área de um retângulo (base x altura).'''
#DaniloSouza 08/04/2020 

import os
import sys

#Função feita para reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#Função para armazenar os textos armazenados em titulos.
def titulo(txt):
    print(txt)
#Função feita para fazer cálculos.
def área(largura, comprimento):
    #Formula para encontrar área.    
    area = largura * comprimento
    #Imprimir a saída com o resultado da área de um retangulo
    print("Área de um retângulo é de %.2fm²" % area)
    #Reinicia o programa
    restart_program()
#Função principal do programa
def main():
    #Ler a entrada da variável da largura
    largura = float(input("Informe a largura: "))
    #Ler a entrada da variável da comprimento
    comprimento = float(input("Informe o comprimento: "))
    #Chamar a função área
    área(largura, comprimento)
#Texto que a função titulo armazena
titulo('Informe o valor em metros!')
#Chama a função principal
main()

