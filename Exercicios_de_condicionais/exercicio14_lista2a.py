def main():
    n1 = int(input("digite ó primeiro número: "))
    n2 = int(input("digite ó segundo número: "))
    n3 = int(input("digite o terceiro número: "))
    n4 = int(input("digite o quarto número: "))
    n5 = int(input("digite o quinto número: "))
    calculo(n1, n2, n3, n4, n5,)
    print('Ultrapassa á média.')


def calculo(n1, n2, n3, n4, n5,):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    print(f'A média entre os números é {media}\nOnde:')
    n1_(n1, media)
    n2_(n2, media)
    n3_(n3, media)
    n4_(n4, media)
    n5_(n5, media)


def n1_(n,media):
    if n > media:
        print(n)
    else:
        return n


def n2_(n, media):
    if n > media:
        print(n)
    else:
        return n


def n3_(n, media):
    if n > media:
        print(n)
    else:
        return n


def n4_(n, media):
    if n > media:
        print(n)
    else:
        return n


def n5_(n, media):
    if n > media:
        print(n)
    else:
        return n


main()
