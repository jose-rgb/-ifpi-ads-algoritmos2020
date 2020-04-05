def main():
    num = float(input('digite um número: '))
    calculo(num)


def calculo(num):
    if num > 0:
        print('O número é positivo.')
    else:
        print('O número é negativo')


main()