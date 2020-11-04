def main():
    
    menu()
    option()
    
def menu():
    print('########## WordPplay ##########\n0-Palavras com mais de 20 letras')
    print('1-selecionar palavras com a letra que se desja.\n2-sair')


def option():

    option = int(input('Digite uma opção: '))

    if option == 0:
        arquivo = open('words.txt')
        for linha in arquivo:
            if len(linha) > 20:
                print(linha.strip())

        arquivo.close()

    elif option == 1:
        arquivo = open('words.txt')
        var = str(input('digite a letra: '))
        for linha in arquivo:
            palavra = linha.strip()
            verificador(palavra, var)
        arquivo.close()

    elif option == 2:
        print('saindo....')

    else:
        print('opção inválida')
        input('<<Enter>> para continuar')


menu()
option()


def verificador(palavra, var):
    for letra in palavra:
        if letra == var:
            print(palavra)
       
        

main()
       
        

