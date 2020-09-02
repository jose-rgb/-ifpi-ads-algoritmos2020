# 1. Leia N e escreva todos os números inteiros de 1 a N.
def main():
    n = float(input("Digite um número: "))
    inicio = 1
    c = 0
    repetidor(n, inicio, c)


def repetidor(n, inicio, c):
    #verificando se n é inteiro ou fracionário
    if int(n) - n == 0:
        n = n
    else:
    
        n = n-1
    while n > inicio:
        inicio += 1
        c += 1
        print(inicio - 1)
    print(">>Anterior ao número {:.1f}, existem {} número(s) inteiros.".format(n, c))


main()

