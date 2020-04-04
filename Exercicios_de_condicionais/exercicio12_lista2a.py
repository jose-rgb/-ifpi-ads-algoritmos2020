def main():
    num = int(input('Digite um número inteiro: '))
    calculo(num)


def calculo(m):
    if m % 2 == 0:
        print(f'O número {m} é par. ')
    else:
        print(f'O número {m} é impar.')


main()


