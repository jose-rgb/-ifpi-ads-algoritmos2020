 #Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
 #Aritmética que tem por valor inicial A0 e razão R.


def main():
    a0 = int(input('Digite o valor inicial: '))
    limite = int(input('digite o limite(quantidade de elementos): '))
    r = int(input('digite a razão: '))
    an = a0 + (limite - 1) * r
    repetidor(a0, r, an)


def repetidor(a0, r, an):
    for i in range(a0, an+1, r):
        print(i)


main()
