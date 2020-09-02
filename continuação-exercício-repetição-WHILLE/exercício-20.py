#20. s = 1/1 - 1/2 + 1/3 ... +/- 1/n
def main():
    n = int(input('Digite N: '))

    c = 1
    resultado = 0
    while c <= n:
        if n < 1:
            print('Digite um número positivo.')
        else:
            if c % 2 == 0:
                resultado -= (1 / c)
            else:
                resultado += (1 / c)
            c += 1
    print(f'{resultado:.2f}')


main()
