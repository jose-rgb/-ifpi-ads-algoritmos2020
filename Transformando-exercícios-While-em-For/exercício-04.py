# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.


def main():
    a0 = int(input('Digite o valor inicial: '))
    limite = int(input('digite o limite(quantidade de elementos): '))
    r = int(input('digite a razão: '))
    an = a0 * r **(limite - 1)
    repetidor(a0, r, an, limite)


def repetidor(a0, r, an, limite):
    c = 1
    for i in range(a0, an+1):
        an = int(a0 * r ** (limite - c))
        c += 1
        if an >= a0:
            print(an)


main()
