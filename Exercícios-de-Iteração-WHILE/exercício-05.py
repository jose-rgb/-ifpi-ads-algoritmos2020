# 5. Leia um número, calcule e escreva seu fatorial.
def main():
    num = int(input('digite um número fatorial: '))
    resultado = num
    r = calculo(num, resultado)
    print('O fatorial de {}! é {}.'.format(num, r))


def calculo(num, resultado):
    while num > 1 and num != 2:
        num -= 1
        resultado *= num
    return resultado


main()
